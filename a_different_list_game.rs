// For: https://open.kattis.com/problems/listgame2

use std::cmp::Ordering;
use std::collections::HashMap;
//use std::collections::HashSet;

const DEBUG: bool = false;

fn get_u64_from_stdin() -> u64 {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed to read");
    buffer.trim().parse::<u64>().expect("String is not a valid u64")
}

// NOTE: 
//   I was stuck on this problem for a while until I realized that I was making a bad assumption. The actual number / 
//   order of each prime factor combination wasn't important, what was important was how they combined & stopped each
//   other from combining. In order to better conceptualize the puzzle I started thinking about the prime factors as 
//   symbols.
//
//   The problem is then reduced into prime factorization, followed by finding the maximum number of unique subsets
//   of the prime factors, using only the same number of each prime factor as it's degree.
fn get_points_old(mut num: u64) -> Vec<u64> {
    let mut out_vec: Vec<u64> = Vec::new();

    let mut inc = 1;
    let mut i = 2_u64;

    // medium performance buff here
    if num % i == 0 {
        if DEBUG { println!("factor {}", i); }

        out_vec.push(i);
        num /= i;
        
        if num % 2 != 0 {
            inc = 2;
        }
    }
    i += 1;

    while i < num + 1 { 
        if num % i == 0 {
            if DEBUG { println!("factor {}", i); }

            out_vec.push(i);
            num /= i;
            
            if num % 2 != 0 {
                inc = 2;
            }
        }

        i += inc;
    }

    out_vec
}

/*
fn get_points_old_fast(mut factors: Vec<u64>) -> Vec<u64> {
    factors.dedup();

    let mut out_vec: Vec<u64> = Vec::new();
    let mut checked: HashSet<u64> = HashSet::new();

    for i in 0..factors.len() {
        for j in i..factors.len() {

        }
    }

    let mut i = 2_u64;
    while i < num + 1 { 
        if num % i == 0 {
            if DEBUG { println!("factor {}", i); }

            out_vec.push(i);
            num /= i;
        }

        i += 1;
    }

    out_vec
}
*/

fn get_prime_factors(mut num: u64) -> HashMap<u64, u64> {
    let mut data_map: HashMap<u64, u64> = HashMap::new();

    let mut i = 2_u64;

    while num % i == 0 {
        if DEBUG { println!("factor {} : {}", i, num); }

        *data_map.entry(i).or_insert(0) += 1;

        num /= i;
    }

    i += 1;

    // small shortcut but should improve performance significantly

    while /*num != 1*/ i < num + 1 {
        while num % i == 0 {
            if DEBUG { println!("factor {} : {}", i, num); }

            *data_map.entry(i).or_insert(0) += 1;

            num /= i;
        }

        i += 2;
    }

    data_map
}

// max at front
fn reverse_sort(a: &u64, b: &u64) -> Ordering {
    if a == b { Ordering::Equal } else if a > b { Ordering::Less } else { Ordering::Greater }
}

// TODO: do the set checking algorithm w/ the function that assigns all permuatations at levels -> i.e sizes.
// Should increase performance since it is bounded by # of factors which is max 49.

// This function just swaps sets of factors so that the smallest set of factors are comprised of the factors with the 
// largest values.
// This does not overflow u64 since there are becoming more small numbers & fewer large numbers.
fn get_points_new(num: u64) -> Vec<u64> {
    let factors_map = get_prime_factors(num);

    if DEBUG { println!("Got the factors! {:?}", factors_map); }

    // i.e the value of the nth factor, as opposed to the number of the nth factor
    let mut factor_values: Vec<u64> = factors_map.keys().cloned().collect();
    let mut factor_degrees: Vec<u64> = factors_map.values().cloned().collect();
    factor_values.sort();
    factor_degrees.sort_by(reverse_sort);

    // build the number with a better order.
    let mut new_num: u64 = 1; // NOTE: WTF, WHY IS NEW NUMBER RANDOM?
    for (i, degree) in factor_degrees.iter().enumerate() {
        new_num *= factor_values[i].pow(*degree as u32);
    }

    if DEBUG { println!("Rebuilt number!"); }

    get_points_old(new_num)
}

fn main() {
    // Note: 10^3 <= num <= 10^15
    let num: u64 = get_u64_from_stdin(); //1099511627776
    println!("{}", get_points_new(num).len());
}