// For: https://open.kattis.com/problems/listgame2

use std::collections::HashSet;

const DEBUG: bool = false;

fn get_u64_from_stdin() -> u64 {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed to read");
    buffer.trim().parse::<u64>().expect("String is not a valid u64")
}

fn get_points(mut num: u64) -> u64 {
    let mut used: HashSet<u64> = HashSet::new();
    let mut points = 0;
    let mut last_counter = 2u64;

    while num >= last_counter { // note: any extra value can be mutliplied to the last factor & it is still optimal. -> this note is probably false.
        for i in 2..(num+1) { 
            if num % i == 0 && !used.contains(&i) {
                if DEBUG { println!("factor {}", i); }

                used.insert(i);
                points += 1;

                last_counter = i + 1;
                num /= i;
                
                break;
            }
        }
    }

    points
}

fn main() {
    // Note: 10^3 <= num <= 10^15
    let num: u64 = get_u64_from_stdin(); //1099511627776
    println!("{}", get_points(num));
}