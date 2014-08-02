$(document).ready(ini);


function ini(){

	var pathArray = window.location.pathname.split('/');
	$('#option_panel').click(function(){go_to_panel(pathArray)});
	$('#option_students').click(function(){go_to_students_list(pathArray)});
	$('#option_contents').click(function(){go_to_contents_list(pathArray)});




}


function go_to_panel(pathArray){

	var classroom = pathArray[3] ;
	$('#option_panel').attr('href','/panel/lista/' + classroom);

}

function go_to_students_list(pathArray){

	var classroom = pathArray[3] ;
	$('#option_students').attr('href','/alumnos/listas/' + classroom);

}


function go_to_contents_list(pathArray){

	var classroom = pathArray[3] ;
	$('#option_contents').attr('href','/contenidos/' + classroom);

}
