$(document).ready(ini);


function ini(){

  $("#select_unit").attr('disabled','disabled');
  $("#select_subject").attr('disabled','disabled');
  
  $('#select_area').change(load_fiters);
  $('#eg7').click(sm);
  
}

                
function sm(){

  $.smallBox({
    title : "Juan Perez necesita ayuda",
    content : "<i class='fa fa-clock-o'></i> <i>2 seconds ago...</i>",
    color : "#296191",
    iconSmall : "fa fa-thumbs-up bounce animated",
    //timeout : 4000
});
}


function load_fiters(){

    var id_area = $(this).val();
    load_filter_subjects(id_area);

        
}

function load_filter_subjects(id_area){
  var cg = $('#code').val();
  var tok = $("#token").attr("value");
  var query = $.ajax({
    //url:"lista/A8o6/materias/",
    url:"lista/"+cg+"/materias/",
    type:'POST',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_area: id_area,
          name: 'y.name',
          id:'y.id',
          
    }, 
    
    "success":function(data){
       
      $('#select_subject').removeAttr('disabled');
      var output_select = "";
      output_select += '<option value="0" selected="" disabled="">Materia</option>'
      for (var y in data["dictionary_subjects"]){
        output_select += "<option value="+(data["dictionary_subjects"][y]['id'])+">";
        output_select += (data["dictionary_subjects"][y]['name']); 
        output_select += "</option>";
        }/*Cierro for dictionary_subjects*/
        $("#select_subject").html(output_select);
      }

       

    })
    $("#select_subject").change(load_units);


}

function load_units(){
  var cg = $('#code').val();
  var id_subject = $(this).val();
  var tok = $("#token").attr("value");  
  var query = $.ajax({
   url:"lista/"+cg+"/unidades/",
    type:'POST',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_subject: id_subject,
          name: 'p.name',
          id:'p.id',
          
          
    }, 
    
    "success":function(data){
       
      $('#select_unit').removeAttr('disabled');
      var output_select_unit="";
      output_select_unit +='<option value="0" selected="" disabled="">Unidad</option>'
      for (var p in data["dictionary_units"]){
        output_select_unit += "<option value="+(data["dictionary_units"][p]['id'])+">";
        output_select_unit += (data["dictionary_units"][p]['name']); 
        output_select_unit += "</option>";
        }/*Cierro for dictionary_subjects*/
        $("#select_unit").html(output_select_unit);
      }

       

    })

    $('#select_unit').change(get_students_data);


}/*cierro funcion load_units*/

function get_students_data () {

    var code_class = $("#code").attr("value");
    var id_unit = $(this).val();
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:"lista/"+code_class+"/alumnos/",
    type:'post',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_unit: id_unit,
          img:'img',
          exercise_id:'exercise_id',
          matriz:'matriz'

    }, 

    "success":function(data){
        create_table_students(data);
      }

    })
  
} /*cierro function get_students_data*/


//<th><a href="javascript:void(0);" class="btn btn-default btn-lg" rel="popover" data-placement="top" data-original-title="<h4>Ejercicio</h4>" data-content="<div class='tab-pane fade in active' id='pop-1'>
//<img src='{% static "img/img.png" %}'></div>" data-html="true">{{e.exercise_id}}</a></th>

function create_table_students (data) {

if(data['type'] == 'success'){  
    var output_thead = "";
    
    output_thead +="<tr>";
    output_thead +="<th>Nombre</th>";                                                   
    output_thead +="<th>Apellido</th>";
    for (var e in data["dictionary_units_exercises"]){
        output_thead += "<th>";  
       // output_thead += '<a href="javascript:void(0);" class="btn btn-default btn-lg" rel="popover" data-placement="top" data-original-title="<h4>Ejercicio</h4>" data-content="' + '<div data-html="true"class=' +"'"+ 'tab-pane fade in active' +"'"+ 'id='+"'"+'pop-1'+"'" +'></div>';
        //output_thead += '<img src="'+ (data["dictionary_units_exercises"][e]['img']) +'" class="img-responsive" ></div>" >';      
        //output_thead += '</a>';
        var contenido = '<div data-html="true" class=' +"'"+ 'tab-pane fade in active' + "'" + 'id='+"'"+'pop-1'+"'" +'><img src="'+ (data["dictionary_units_exercises"][e]['img']) +'" class="img-responsive"></div>'
        output_thead += '<a href="javascript:void(0);" class="btn btn-default btn-lg" rel="popover" data-placement="top" data-original-title="<h4>Ejercicio</h4>" data-content="'+ contenido +'"></a>'; 
        output_thead += "</th>";  
       // output_thead += (data["dictionary_units_exercises"][e]['exercise_id']); 
        //output_thead += "</a></th>";
    }
    output_thead +="</tr>";
    
  var output = "";
  
  for (var x in (data["matriz"])){

   output += "<tr>"; 

    for (var y = 0; y < (data["matriz"])[x].length ; y++){

        output += "<td>";
        output += (data["matriz"])[x][y];
        output += "</td>";


   }/*cierro for dictionary_students*/
    
    output += "</tr>";

 }
      
    if (output != ""){
      $("#dt_alumnos > tbody ").html(output);
      $("#dt_alumnos > thead").html(output_thead);
     // var table = $('#dt_alumnos').DataTable();
     // table.order( [ 1, 'asc' ] );
      //table.draw();
    //  $('#dt_alumnos').draw();
     // $('#dt_alumnos').order( [ 1, 'asc' ] )
      $('#dt_alumnos').dataTable();
    }

    
  }

}