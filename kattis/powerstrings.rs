// unsolved

fn get_string_from_stdin() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed to read line from stdin");
    buffer.trim().to_string() // TODO: make sure this doesn't suck
}

// This function finds the number of times the string 'a' repeats.
// ex: ababab -> 3
fn string_repetitions(string: &str) -> u32 {
    let bytes = string.as_bytes();
    let string_len = bytes.len();

    // NOTE: for some strings, string_len/2 can be minimized to string_len/3 and perhaps even further
    for step in 1..(string_len/2)+1 {
        if string_len % step == 0 {
            let mut is_valid = true;

            for i in step..string_len {
                let head = bytes[i % step];
                if bytes[i] != head {
                    is_valid = false;
                    break;
                }
            }

            if is_valid {
                return (string_len / step) as u32; // how many steps are taken
            }
        }
    }

    1 // means no internal repetitions
}

fn is_repetitive(bytes: &[u8], step: usize) -> bool {
    let string_len = bytes.len();

    for i in step..string_len {
        let head = bytes[i % step];
        if bytes[i] != head {
            return false;
        }
    }

    true
}

fn string_repetitions_f(string: &str) -> u32 {
    let bytes = string.as_bytes();
    let string_len = bytes.len();

    let mut valid_steps: Vec<usize> = Vec::new();
    for step in 1..((string_len as f64).sqrt().floor() as usize)+1 {
        if string_len % step == 0 {
            valid_steps.push(step);
            valid_steps.push(string_len / step);
        }
    }
    valid_steps.sort(); // TODO: remove the sort by having two vectors?

    for step in valid_steps {
        if is_repetitive(bytes, step) {
            return (string_len / step) as u32; // how many steps are taken
        }
    }

    1 // means no internal repetitions
}

/*
// breaks the string into duplicate sections of varying sizes -> recursive
fn string_repetitions_break(string: &str) -> u32 {
    let bytes = string.as_bytes();
    let string_len = bytes.len();

    // NOTE: needs this section first
    let mut valid_steps: Vec<usize> = Vec::new();
    for step in 1..((string_len as f64).sqrt().floor() as usize) {
        if string_len % step == 0 {
            valid_steps.push(step);
            valid_steps.push(string_len / step);
        }
    }
    valid_steps.sort(); // TODO: remove the sort by having two vectors?

    // NOTE: for some strings, string_len/2 can be minimized to string_len/3 and perhaps even further
    for step in 1..(string_len/2)+1 {
        if string_len % step == 0 {
            let mut is_valid = true;

            for offset in 0..step { // checks if the string is split into groups of size $split
                let head = bytes[offset];

                for rep in (step + offset..string_len).step_by(step) {
                    if bytes[rep] != head {  // repetitive pattern is not consistent
                        is_valid = false;
                        break;
                    }
                }

                if !is_valid {
                    break;
                }
            }

            if is_valid {
                return (string_len / step) as u32; // how many steps are taken
            }
        }
    }

    1 // means no internal repetitions
}
*/

// This is the top down left-recursive algorithm. -> the main pass will recurse with any pn, but any other passes will
// only recurse down with that specific number.
fn string_repetitions_reuse(string: &str) -> u32 {
    0
}


// !!!!!!!!! TRY THIS NEXT !!!!!!!!!!!!
// TODO: Try an algorithm which recursively builds patterns from the ground up (since patterns are made from the ground up).
//       this way we only need to do exactly N reads. -> maybe all the sections can communicate through a hashmap-like bus.

fn get_input_vector() -> Vec<String> {
    let mut cases: Vec<String> = Vec::new();
    loop {
        let s = get_string_from_stdin();
        if s == "." {
            break;
        } else {
            cases.push(s);
        }
    }
    cases
}

fn main() {
    let cases: Vec<String> = get_input_vector();

    for line in cases {
        println!("{}", string_repetitions_f(&line));
    }
}