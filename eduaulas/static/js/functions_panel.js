$(document).ready(ini);


function ini(){

  $("#select_unit").attr('disabled','disabled');
  $("#select_subject").attr('disabled','disabled');
  $('#refresh_results').attr('disabled','disabled');
  $('#load_suggestions').attr('disabled','disabled');
  $('#refresh_results').click(get_students_data);
  $('#select_area').change(load_fiters);
  $('#load_suggestions').click(function(){search_for_suggestions(0)});
  $('#next').click( function(){search_for_suggestions(1)});
  $('#prev').click( function(){search_for_suggestions(2)});
  
}
var student= 0; 
     
function search_for_suggestions(pos){

  var code_class = $("#code").attr("value");
  var id_unit = $('#select_unit').val();
  var tok = $("#token").attr("value");
  var query = $.ajax({
  url:code_class+"/sugerencias/",
  //url:"lista/"+code_class+"/sugerencias/",
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

     if (student == student_cont -1){
        $('#next').addClass('disabled');
           
      }
    }
               
 
    if ((pos==2) && (student >0 )){
      student = student - 1;
      load_suggestions(data,student);
      $('#next').removeClass('disabled');

     if (student == 0){
        
        $('#prev').addClass('disabled');   
          }
    }
 

}/**close function pagination*/

function load_suggestions(data,student){

var cont = '';
cont =(data["matriz_suggestions_students"])[student].length;
var output ='';
 
    for (var y = 1; y < cont; y++){
      if (y == 1){

      output += "<h6>Alumno:";
      output += (data["matriz_suggestions_students"])[student][y];
      output += "<br></h6>";
      }
      else{
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
    url:"/panel/lista/"+cg+"/materias/",
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
    url:cg+"/unidades/",
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
      $('#select_unit').change(get_students_data);

       
}
    })

    

}/*cierro funcion load_units*/

function getTime(){

 var d = new Date();
    var hours = d.getHours();
    var minutes = d.getMinutes();
    var seconds = d.getSeconds();
    var year =d.getFullYear();
    var month = (d.getMonth()+1);
    var day = d.getDate();   
    var date = "";
    var str_hours = new String(hours);
    var str_minutes = new String(minutes);
    var str_seconds = new String(seconds);
    var str_year = new String(year);
    var str_month = new String(month);
    var str_day = new String(day);  

    if (str_day.length == 1){
       date += '0' + str_day;
    }
    else{
      date += str_day;
    }

    date += '/';
        
    if (str_month.length == 1){
       date += '0' + str_month;
       
    }
    else{
      date += str_month;
    }

    date += '/';

    if (str_year.length == 1){
       date += '0' + str_year;
    }
    else{
      date += str_year;
    }

    date += '-';

    if (str_hours.length == 1){
       date += '0' + str_hours;
    }
    else{
      date += str_hours;
    }

    date += '-';

    if (str_minutes.length == 1){
       date += '0' + str_minutes;
    }
    else{
      date += str_minutes;
    }

    date += '-';

    if (str_seconds.length == 1){
       date += '0' + str_seconds;
    }
    else{
      date += str_seconds;
    }

   


    $('#last_update').html(date)

}

function get_students_data () {
  
    getTime();
    var code_class = $("#code").attr("value");
    var id_unit = $('#select_unit').val();
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:code_class+"/alumnos/",
    type:'post',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_unit: id_unit,
          img:'img',
          exercise_id:'exercise_id',
          matriz:'matriz',
          results_exist:'results_exist',
          students_exist:'students_exist',
          id:'id',
          time_to_update_panel:'time_to_update_panel'

    }, 

    "success":function(data){
        create_table_students(data);
        var time = (data['time_to_update_panel'])*(1000*60);
        setInterval(get_students_data, time);
       $('#refresh_results').removeAttr('disabled','disabled');
      }

    })
  
} /*cierro function get_students_data*/



function create_table_students (data) {

var code_class = $("#code").attr("value");
if(data['type'] == 'success'){  
    var output_thead = "";
    
    var results_exist = data["results_exist"];
    var students_exist = data["students_exist"];

    if (results_exist == 'yes'){

       $('#load_suggestions').removeAttr('disabled','disabled');

    }
    
  
    output_thead +='<tr>';
    output_thead +='<th>Nombre</th>';                                                   
    for (var e in data["dictionary_units_exercises"]){ 
        output_thead += '<th>';  
        var contenido = "<div><a target = 'blank' href='/contenidos/ejercicio/"+code_class+"/"+ (data["dictionary_units_exercises"][e]["id"]) +"'><img src=" + "'" + (data["dictionary_units_exercises"][e]["img"]) +"'" + " ></a>";
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
    tr_color = (data["matriz"])[x][aux+1];
    output += "<tr>";
    if (tr_color == 'orange'){
       output += "<tr class='tr_orange'>";  
    }

    if (tr_color == 'green'){
       output += "<tr class='tr_green'>";  
    }
  
    if (tr_color == 'red'){
       output += "<tr class='tr_red'>";  
    }
    
      
    
  
    
    var average = 0;
    var results_quantity = 0;
    var points_sum = 0;

    for (var y = 1; y < (data["matriz"])[x].length-1; y++){
      
        if (y == 1){
          output += "<td ><a target='blank' href='/alumnos/info_alumno/"+code_class+"/"+(data["matriz"])[x][0]+"'>"+(data["matriz"])[x][y]+"</a></td>";}
          
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

  $("tr#fil1").attr("style","background-color:blue;");

}/*close function tr_color*/