// For: https://open.kattis.com/problems/listgame2

use std::collections::HashSet;
use rand::seq::SliceRandom;
//use rand::Rng;

const DEBUG: bool = false;

fn get_points(mut num: u64) -> u64 {
    let mut used: HashSet<u64> = HashSet::new();
    let mut points = 0;
    let mut last_counter = 2u64;

    while num >= last_counter { // note: any extra value can be mutliplied to the last factor & it is still optimial.
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

// from https://gist.github.com/qolop/71ef78c394db822756d58cac9993db77
fn get_factors_functional(n: u64) -> Vec<u64> {
    (1..n + 1).into_iter().filter(|&x| n % x == 0).collect::<Vec<u64>>()
}

// this works but is pretty slow
fn points_from_factors(mut factors: Vec<u64>) -> u64 {
    let mut points: u64 = 0;

    // TODO: later -> do optimal permuatations -> start with smallest subset of each size, then choose the smallest & redo until all subsets are too small.

    /*
    for i in 2..*factors.iter().max().expect("factors is empty") {
        if factors.contains(&i) {
            let vec = get_factors_functional(i);

            // removes from factors the elements in vec. if factors has multiple versions of that element, it only removes one.
            for item in vec {
                let index = factors.iter().position(|x| *x == item);
                match index {
                    Some(i) => { factors.remove(i); },
                    None => (),
                }
            }

            points += 1;
        }
    }*/

    points
}

fn main() {
    let primes = vec![2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131];
    let small_primes = vec![2,3,5,7,11,13,17,19,23];

    println!("tests 1:");
    for _iteration in 0..1000/*00*/ {
        // Note: 10^3 <= num <= 10^15
        let mut num: u64 = 1;
        let mut prime_count = 0;
        while prime_count < 8 {
            let el = primes.choose(&mut rand::thread_rng()).unwrap();
            if num % el != 0 {
                num *= el;
                prime_count += 1
            }

            if num > 10_u64.pow(15) {
                break;
            }
        }

        if num > 10_u64.pow(15) || num < 1000 {
            //println!("skipped\t{}", num);
            continue;
        }

        if get_points(num) != 8 {
            println!("failed ->\t{}", num);
        }
    }

    println!("tests 2:");
    for _iteration in 0..100 {
        // Note: 10^3 <= num <= 10^15
        let mut num: u64 = 1;
        let mut factors: Vec<u64> = Vec::new();
        while factors.len() < 16 {
            let el = small_primes.choose(&mut rand::thread_rng()).unwrap();
            num *= el;
            factors.push(*el);

            // catches overflows early
            if num > 10_u64.pow(15) {
                break;
            }
        }

        if num > 10_u64.pow(15) || num < 1000 {
            //println!("skipped\t{}", num);
            continue;
        }

        let points = points_from_factors(factors);
        if get_points(num) != points {
            println!("failed ->\t{}\t| {} != {}", num, get_points(num), points);
        } else {
            println!("succeeded ->\t{}\t| {} != {}", num, get_points(num), points);
        }
    }
    
    println!("done tests");
}

// (2) (2 2) (3) 3 3 (5) 5 5 7 