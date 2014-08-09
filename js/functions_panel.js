$(document).ready(ini);


function ini(){

  $("#select_unit").attr('disabled','disabled');
  $("#select_subject").attr('disabled','disabled');
  $('#refresh_results').attr('disabled','disabled');
  $('#load_suggestions').attr('disabled','disabled');
  $('#select_area').change(load_fiters);
  $('#load_suggestions').click(function(){search_for_suggestions(0)});
  $('#next').click( function(){search_for_suggestions(1)});
  $('#prev').click( function(){search_for_suggestions(2)});
 // $('#eg7').click(sm);
  

  ///setInterval(check_students_results_status,10000);
}
var student= 0; 
     
function search_for_suggestions(pos){
 //alert(pos);
 
  var code_class = $("#code").attr("value");
  var id_unit = $('#select_unit').val();
  //alert(id_unit2);
  var tok = $("#token").attr("value");
  var query = $.ajax({
  url:"lista/"+code_class+"/sugerencias/",
  type:'POST',
  dataType:"json",
  data:{
        csrfmiddlewaretoken: tok,
        state:'inactive',
        id_unit: id_unit,
        matriz_suggestions_students:'matriz_suggestions_students'

  }, 

  "success":function(data){
     
      pagination(data,pos);
    }

  })



}/*close function load_suggestions*/


function pagination(data,pos){

var student_cont = '';
student_cont =(data["matriz_suggestions_students"]).length;


  if (pos==0){

      student = 0;
      load_suggestions(data,student);
      $('#next').removeClass('disabled');
      $('#prev').addClass('disabled');
    }

    if (pos==1) {
      $('#prev').removeClass('disabled');
      student = student + 1;
      load_suggestions(data,student);
      //alert('estudiante' + student + 'cont'+student_cont);
     if (student == student_cont -1){
        $('#next').addClass('disabled');
           
          }
    }
               
 
    if ((pos==2) && (student >0 )){
      student = student - 1;
      load_suggestions(data,student);
      $('#next').removeClass('disabled');
   //  alert(student);
     if (student == 0){
        
        $('#prev').addClass('disabled');   
          }
    }
 

}/**close function pagination*/

function load_suggestions(data,student){

var cont = '';
cont =(data["matriz_suggestions_students"])[student].length;
var output ='';
   // alert(student);
    for (var y = 1; y < cont; y++){
      if (y == 1){

      output += "<h6>Alumno:";
      output += (data["matriz_suggestions_students"])[student][y];
      output += "<br></h6>";
      }else{
      output += (data["matriz_suggestions_students"])[student][y];
      
      }
    }

  $('#content_suggestions').html(output);
  
  
}/*function load_suggestions*/


function load_fiters(){

    var id_area = $(this).val();
    load_filter_subjects(id_area);

        
}

function load_filter_subjects(id_area){
  var cg = $('#code').val();
  var tok = $("#token").attr("value");
  var query = $.ajax({
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
   
    //setInterval(get_students_data,5000);
  //  setInterval(check_students_results_status,10000);


}/*cierro funcion load_units*/

function get_students_data () {

    var code_class = $("#code").attr("value");
    var id_unit = $('#select_unit').val();
    //alert(id_unit2);
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
        $('#refresh_results').click(get_students_data);
        $('#refresh_results').removeAttr('disabled','disabled');
        $('#load_suggestions').removeAttr('disabled','disabled');

        //$('#prev').attr('disabled','disabled');
      }

    })
  
} /*cierro function get_students_data*/



function create_table_students (data) {

if(data['type'] == 'success'){  
    var output_thead = "";
    
    output_thead +='<tr>';
    output_thead +='<th>Nombre</th>';                                                   
    for (var e in data["dictionary_units_exercises"]){ 
        output_thead += '<th>';  
        var contenido = "<div><a target = 'blank' href='/contenidos/ejercicio/"+ (data["dictionary_units_exercises"][e]["exercise_id"]) +"'><img src=" + "'" + (data["dictionary_units_exercises"][e]["img"]) +"'" + " ></a>";
        var contenido2 = "<h4>Ejercicio Nº "+ (data["dictionary_units_exercises"][e]["exercise_id"]) +"</h4>";
        output_thead += '<a href="javascript:void(0);"  rel="popover"  data-html="true" data-placement="top" data-original-title="'+ contenido2 +'" data-content="'+ contenido +'">Ej.'+(data["dictionary_units_exercises"][e]["exercise_id"])+'</a>'; 
        output_thead += '</th>';  
    }
    output_thead +='</tr>';
    
  var output = "";
  var tr_cont = 0;
  var tr_color = "";
  var aux = 0;
  for (var x in (data["matriz"])){
    tr_cont++;
    aux = (data["matriz"]).length;
    tr_color = (data["matriz"])[x][aux + 2];
    if (tr_color == 'green'){
       output += "<tr class='tr_green'>";  
    }else{
    if (tr_color == 'red'){
       output += "<tr class='tr_red'>";  
    }else{
        output += "<tr>";
    }}
    
    var average = 0;
    var results_quantity = 0;
    var points_sum = 0;

    for (var y = 1; y < (data["matriz"])[x].length-1; y++){
      
        if (y == 1){
          output += "<td ><a target='blank' href='/alumnos/info_alumno/"+(data["matriz"])[x][0]+"'>"+(data["matriz"])[x][y]+"</a></td>";}
          
        else {
          
          results_quantity ++;
          points_sum += (data["matriz"])[x][y];
          average = points_sum / results_quantity;
          output += '<td>';
          output +=  (data["matriz"])[x][y];
          output += '</td>';}


   }/*cierro for dictionary_students*/
    
    output += "</tr>";
    


 }
      
    if (output != ""){

      $("#dt_alumnos > tbody ").html(output);
      $("#dt_alumnos > thead").html(output_thead);
   

    }
  }

}/*close function create_table_students*/

function tr_color(results_quantity,average,tr_cont){
 // alert('hola');
 // $("#fil1").attr("class","tr_red");
 //$("#hola").attr("style","tr_red");
  $("tr#fil1").attr("style","background-color:blue;");
}/*close function tr_color*/