

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

// TODO: check this.
fn is_repetitive(bytes: &[u8], step: usize) -> bool {
    let string_len = bytes.len();

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
            return true; // how many steps are taken
        }
    }

    return false;
}

// !!!!!!!!! TRY THIS NEXT !!!!!!!!!!!!
// TODO: Try an algorithm which recursively builds patterns from the ground up (since patterns are made from the ground up).
//       this way we only need to do exactly N reads. -> maybe all the sections can communicate through a hashmap-like bus.

// TODO: try this but recursive

// works line binary search
fn string_repetitions_v2(string: &str) -> u32 {
    let bytes = string.as_bytes();
    let string_len = bytes.len();

    // TODO: does this section take too long?
    // TODO: go to isqrt & add both step and string_len / step
    let mut valid_steps: Vec<usize> = Vec::new();
    for step in 1..(string_len/2)+1 {
        if string_len % step == 0 {
            valid_steps.push(step);
        }
    }
    valid_steps.push(string_len);

    println!("{:?}", valid_steps);

    let mut beg = 0;
    let mut end = valid_steps.len() - 1;

    while (end - beg) != 0 {
        let stepi = (beg + end) / 2;
        let step = valid_steps[stepi];

        if is_repetitive(bytes, step) {
            end = stepi; // includes self
        } else {
            beg = beg + 1;
        }
    }

    (string_len / valid_steps[(beg + end) / 2]) as u32
}

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
        println!("{}", string_repetitions_v2(&line));
    }
}