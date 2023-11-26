(* util *)

let print_list list =
  List.iter (Printf.printf "%d ") list;
  Printf.printf "\n"

let inc = fun x -> x + 1

let any_mod list i =
  List.exists (fun m -> i mod m = 0) list

(* const *)

let limit = 1000

(* behaviour *)

let () = 
  let nums = List.init (limit - 1) inc in
  let multiples_of_3_5 = List.filter (any_mod [3; 5]) nums in 
  let result = List.fold_left ( + ) 0 multiples_of_3_5 in
    print_int result;
    print_endline ""
