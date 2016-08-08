let main () = begin
	let edges = ref [] in
	let return = ref [] in
	let no_edge = ref [] in
	let unalt_start = ref [] in
	let unalt_end = ref [] in
	

try
	while true do 
		let line = String.trim (read_line()) in
		let line2 = String.trim (read_line()) in
		unalt_end := line :: !unalt_end ;
		unalt_start := line2 :: !unalt_start ;
		edges := (line, line2) :: !edges
done

with _ -> begin
	List.iter (fun start ->
		if not (List.mem start !unalt_end) then no_edge := start :: !no_edge
	) !unalt_start ;

	while !no_edge <> [] do
		let sorted_no_edge = List.sort compare !no_edge in
		no_edge := sorted_no_edge ;
		let start = List.hd !no_edge in
		let new_no_edge = List.filter (fun x -> x <> start) !no_edge in
		no_edge := new_no_edge ;
		return := !return @ [start] ;

		List.iter (fun (a,b) ->
			if b = start then 
				let new_edges = List.filter (fun x -> x <> (a,b)) !edges in
				edges := new_edges ; 
			
				unalt_end := [] ;
				List.iter (fun (a,b) ->
					unalt_end := a :: !unalt_end;
				) !edges;

				if not (List.mem a !unalt_end) then no_edge := !no_edge @ [a] ;

		) !edges;

		
	done ;

	if (!edges <> []) then print_string "cycle"

	else List.iter (fun l -> print_string (l ^ "\n")) !return

end

end ;;
main () ;;