// Import dlsym to find the original function
#include <dlfcn.h>
// Import uint32_t for a specifically 32-bit int
#include <stdint.h>

// Set up a function with the same signature as the real function
uint32_t random_uint32()
{
    // Set up a pointer that we use to store the real function
    uint32_t (*real_random)();
    // Store the result in a uint32 when we get it
    uint32_t result;
    // Find the real function and store it in the pointer
    real_random = dlsym(RTLD_NEXT, "random_uint32");
    // Run the real function
    result = real_random();
    // Add 17
    result += 17;
    // Return the original result + 17
    return result;
}
