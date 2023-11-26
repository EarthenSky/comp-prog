(* util *)

let rec fold_until f p acc seq = match seq () with
  | Seq.Cons (x, seq) when p x -> acc
  | Seq.Cons (x, seq) -> fold_until f p (f acc x) seq
  | Seq.Nil -> acc

(* behaviour *)

module Number = struct
  type t = int
  let compare = compare
end

module Cache = Map.Make (Number)

let () = 
  let cache = Cache.empty in
  let cache = Cache.add 0 1 cache in
  let cache = ref (Cache.add 1 2 cache) in
  
  let rec fib x = 
    match !cache |> Cache.find_opt x with
    | Some x -> x
    | None ->
      match x with
      | 0 -> 1
      | 1 -> 2
      | _ ->
        let fibx = (fib (x - 1)) + (fib (x - 2)) in
          cache := Cache.add x fibx !cache; (* aaaa, it's not purely functional! (haskell programmer dies) *)
          fibx in
  
  let rec fib_list n = fun () -> Seq.Cons (fib n, fib_list (n + 1)) in
  let even_fib = Seq.filter (fun a -> a mod 2 == 0) (fib_list 0) in
  let result = fold_until ( + ) (fun v -> v > 4_000_000) 0 even_fib in
    print_int result;
    print_endline ""
