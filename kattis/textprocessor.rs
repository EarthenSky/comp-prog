// unsolved

fn get_u64_from_stdin() -> u64 {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed to read");
    buffer.trim().parse::<u64>().expect("String is not a valid u64")
}

fn main() {
    println!("Hello World!");
}