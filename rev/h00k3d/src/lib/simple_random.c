// NOTE
// This does not have parity with the Python version but is arguably better
#include <stdint.h>
#include <stdlib.h>

// === PRIVATE ===

// 32-bit LFSR
typedef struct strLFSR {
    uint32_t reg;
    uint32_t internal_tap_mask; // For each bit:
    uint32_t external_tap_mask; // 1 = tap, 0 = not tap
} LFSR;

typedef struct strExternalTaps {
    uint32_t value;
    uint32_t mask;
} ExternalTaps;

// Returns external taps
ExternalTaps LFSR_step(LFSR *lfsr, ExternalTaps sources) {
    ExternalTaps external_taps = (ExternalTaps) {lfsr->reg, lfsr->external_tap_mask};

    uint8_t new_first = 0;
    // XOR all internal taps together to get a new first bit
    for (uint8_t bit_pos = 0; bit_pos < 32; bit_pos++) {
        uint8_t current_mask = (lfsr->internal_tap_mask >> bit_pos) & 1;
        
        if (current_mask) {
            uint8_t current_bit = (lfsr->reg >> bit_pos) & 1;
            new_first ^= current_bit;
        }
    }
    
    for (uint8_t bit_pos = 0; bit_pos < 32; bit_pos++) {
        uint8_t current_mask = (sources.mask >> bit_pos) & 1;
        
        if (current_mask) {
            uint8_t current_bit = (sources.value >> bit_pos) & 1;
            new_first ^= current_bit;
        }
    }
    
    // This should be the case anyway but it was in the Python code
    new_first &= 1;
    
    lfsr->reg = (lfsr->reg >> 1) | (new_first << 31);
    
    return external_taps;
}

ExternalTaps LFSR_get_external_taps(LFSR *lfsr) {
    return (ExternalTaps) {lfsr->reg, lfsr->external_tap_mask};
}

// 255 = error
uint8_t ExternalTaps_get_index(ExternalTaps taps, uint8_t index) {
    uint8_t at_index = 255;
    for (uint8_t i = 0; i < 32; i++) {
        if ((taps.mask >> i) & 1) {
            at_index++;
        }
        if (at_index == index) {
            return (taps.value >> i) & 1;
        }
    }
    return 255;
}

LFSR *lfsr1;
LFSR *lfsr2;
ExternalTaps taps1;
ExternalTaps taps2;


// === PUBLIC ===

uint8_t generate() {
    // There's currently no error checking here
    uint32_t input_taps_1 = ExternalTaps_get_index(taps2, 2) & ExternalTaps_get_index(taps2, 1);
    uint32_t input_taps_2 = ExternalTaps_get_index(taps2, 1);
    uint32_t input_taps_3 = ExternalTaps_get_index(taps2, 0) & ExternalTaps_get_index(taps2, 1);

    uint32_t input_taps = (input_taps_1 << 2) | (input_taps_2 << 1) | input_taps_3;
    ExternalTaps tappified_taps = (ExternalTaps) {input_taps, 7}; // The mask is just 0b111
    
    taps1 = LFSR_step(lfsr1, tappified_taps);
    
    input_taps_1 = ExternalTaps_get_index(taps1, 0) & ExternalTaps_get_index(taps1, 1);
    input_taps_2 = ExternalTaps_get_index(taps1, 2);
    input_taps_3 = 1 ^ (ExternalTaps_get_index(taps1, 2) & ExternalTaps_get_index(taps1, 0));
    
    input_taps = (input_taps_1 << 2) | (input_taps_2 << 1) | input_taps_3;
    tappified_taps = (ExternalTaps) {input_taps, 7};
    
    taps2 = LFSR_step(lfsr2, tappified_taps);
    
    return ExternalTaps_get_index(taps1, 2) ^ ExternalTaps_get_index(taps2, 1) ^ ExternalTaps_get_index(taps1, 0);
}

void discard(size_t amount) {
    for (size_t i = 0; i < amount; i++) {
        generate();
    }
}

void initialise(uint64_t seed) {
    // Seed the LFSRs
    lfsr1->reg = seed >> 32;
    lfsr2->reg = seed & (0xFFFFFFFF);
    
    // Discard 4096 bits to initialise
    discard(4096);
    
    taps2 = (ExternalTaps) {lfsr2->reg, lfsr2->external_tap_mask};
}
char random_char() {
    char c = 0;
    for (uint8_t i; i < sizeof(char) * 8; i++) {
        c |= generate();
        c <<= 1;
    }
    return c;
}
int32_t random_int32() {
    int32_t c = 0;
    for (uint8_t i = 0; i < sizeof(int32_t) * 8; i++) {
        c |= generate();
        c <<= 1;
    }
    return c;
}
uint32_t random_uint32() {
    uint32_t c = 0;
    for (uint8_t i = 0; i < sizeof(uint32_t) * 8; i++) {
        c |= generate();
        c <<= 1;
    }
    return c;
}

void __attribute__((constructor)) library_init() {
    lfsr1 = malloc(sizeof(LFSR));
    lfsr2 = malloc(sizeof(LFSR));
    
    // Set up the LFSRs
    lfsr1->internal_tap_mask = 0b00110010000010000000000010000000;
    lfsr1->external_tap_mask = 0b00000000000000010000000010000010;
    lfsr2->internal_tap_mask = 0b00000000000101001000001000100000;
    lfsr2->external_tap_mask = 0b00100001100000000000000000000000;
    // They need to be seeded manually still
}

void __attribute__((destructor)) library_cleanup() {
    free(lfsr1);
    free(lfsr2);
}
