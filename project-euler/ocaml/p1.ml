(* util *)

let print_list list =
  List.iter (Printf.printf "%d ") list;
  Printf.printf "\n"

(* const *)
let limit = 1000

(* behaviour *)

let any_mod list i =
  List.exists (fun m -> i mod m = 0) list

let () = 
  let nums = (List.init (limit - 1) (fun x -> x + 1)) in
  let multiples_3_5 = List.filter (any_mod [3; 5]) nums in 
    print_int (List.fold_left ( + ) 0 multiples_3_5);
    print_endline ""
