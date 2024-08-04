use std::env;

fn main() {
    let dir = env::var("CARGO_MANIFEST_DIR").unwrap();
    println!("cargo:rustc-link-search={}", dir);
    println!("cargo:rustc-link-search={}/../lib/", dir);
    println!("cargo:rustc-link-search={}/../static/", dir);
}