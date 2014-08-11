$(document).ready(ini);


function ini(){

	var pathArray = window.location.pathname.split('/');
	$('#option_panel').click(function(){go_to_panel(pathArray)});
	$('#option_students').click(function(){go_to_students_list(pathArray)});
	$('#option_contents').click(function(){go_to_contents_list(pathArray)});
	$('#option_stats_by_topic').click(function(){go_to_stats_by_topics(pathArray)});
	$('#option_stats_by_learning_profiles').click(function(){go_to_stats_by_learning_profiles(pathArray)});




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
	$('#option_contents').attr('href','/contenidos/lista/' + classroom);

}

function go_to_stats_by_learning_profiles(pathArray){

	var classroom = pathArray[3] ;
	$('#option_stats_by_learning_profiles').attr('href','/alumnos/estadisticas_por_perfiles/' + classroom);

}

function go_to_stats_by_topics(pathArray){

	var classroom = pathArray[3] ;
	$('#option_stats_by_topic').attr('href','/alumnos/estadisticas_por_areas/' + classroom);

}