$(document).ready(ini);


function ini(){

	
	get_data();
	
}



function get_data () {
	
    var code_class = $("#code").attr("value");
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:"/alumnos/estadisticas_por_areas/"+code_class+"/obtener" ,
    type:'POST',
    dataType:"json",
    data:{
    	  csrfmiddlewaretoken: tok,
          state:'inactive',
          matriz:'matriz'

    }, 

    "success":function(data){
       draw_stats(data);

      }

    })
  
} /*cierro function get_students_data*/


function draw_stats(data){
	$('#stat_by_topic').html('<div class="sparkline txt-color-red display-inline" data-sparkline-piesize="275px" data-sparkline-offset="90" data-sparkline-type="pie">54,6,12</div>');

	var output = '';
	output = '';
	//output += ' <div class="sparkline txt-color-red display-inline" data-sparkline-type="pie" data-sparkline-offset="90" data-sparkline-piesize="275px">';
	//output+= 54 6 12;
	 for (var x in (data["matriz"])){
	 	//output +=  (data["matriz"])[x][1] +',';

	         // alert(output);
	    for (var y = 0; y < (data["matriz"])[x].length; y++){
	          	          
	          
	     
	}/*cierro for dictionary_students*/
}

//output += '</div>';
//alert(output);	

	//$('#stat_by_topic').html('<div class="sparkline txt-color-red display-inline" data-sparkline-piesize="275px" data-sparkline-offset="90" data-sparkline-type="pie">54,6,12</div>');


}/*close draw_stats */