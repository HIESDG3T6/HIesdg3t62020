<?php

require 'token_generator.php';
require 'priaid_client.php';

class Symptoms
{
    public $config;
    public $diagnosisClient;
    
    function __construct()
    {
        $this->config = parse_ini_file("config.ini");
    }
    
    public function checkRequiredParameters()
    {
        $pass = true;
        
        if (!isset($this->config['username']))
        {
            $pass = false;
            print "You didn't set username in config.ini" ;
        }

        if (!isset($this->config['password']))
        {
            $pass = false;
            print "You didn't set password in config.ini" ;
        }
            
        if (!isset($this->config['authServiceUrl']))
        {
            $pass = false;
            print "You didn't set authServiceUrl in config.ini" ;
        }

        if (!isset($this->config['healthServiceUrl']))
        {
            $pass = false;
            print "You didn't set healthserviceUrl in config.ini" ;
        }
         
        return $pass;
    }
    
    public function authorize()
    {
        if (!$this->checkRequiredParameters())
            return;
        
        $tokenGenerator = new TokenGenerator($this->config['username'],$this->config['password'],$this->config['authServiceUrl']);
        $token = $tokenGenerator->loadToken();
        
        if (!isset($token))
            exit();

        $this->diagnosisClient = new DiagnosisClient($token, $this->config['healthServiceUrl'], 'en-gb');

    }
}
$Symptoms = new Symptoms();
$Symptoms->authorize();

// $test = $Symptoms->diagnosisClient->loadDiagnosis([10], 'Male', 2001);
// var_dump($test);
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width">

    <title>Symptoms</title>

    <link rel="stylesheet" href="">
    <!--[if lt IE 9]>
        <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <!-- Bootstrap libraries -->
    <meta name="viewport" 
        content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
    integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" 
    crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script 
    src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    
    <script
    src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"
    integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut"
    crossorigin="anonymous"></script>

</head>
<body>
  <div id="symptomchecker" class="container">
    <form id="symptomsForm">
      <strong>Year of Birth</strong> <input name="yearofbirth" type="text" id="yearofbirth" class="form-control" required><br><br>

      <strong>Gender: </strong>&nbsp
      <input type="radio" id="male" name="gender" class ="gender" value="Male" required><label for='male'>&nbspMale</label></input>&nbsp&nbsp
      <input type="radio" id="female" name="gender" class ="gender" value="Female" required><label for='female'>&nbspFemale</label></input><br><br>

      <strong>Select symptoms:</strong>
      <div class="form-check">
        <table id='symptoms'>
          <?php
            $symptomlist = $Symptoms->diagnosisClient->loadSymptoms();
            // var_dump($bodyLocations);
            for ($i=0; $i<count($symptomlist); $i+=4){
              $row = '';
              $id = $symptomlist[$i]['ID'];
              $symptomName = ucfirst($symptomlist[$i]['Name']);
              $row .= "<td width=300><input type='checkbox' name='symptoms[]' id=$id class='symptom' value=$id><label for=$id>$symptomName</label></td>";

              if ($i+1<count($symptomlist)){
                $id = $symptomlist[$i+1]['ID'];
                $symptomName = ucfirst($symptomlist[$i+1]['Name']);
                $row .= "<td width=300><input type='checkbox' name='symptoms[]' id=$id class='symptom' value=$id><label for=$id>$symptomName</label></td>";
              }
              
              if ($i+2<count($symptomlist)){
                $id = $symptomlist[$i+2]['ID'];
                $symptomName = ucfirst($symptomlist[$i+2]['Name']);
                $row .= "<td width=300><input type='checkbox' name='symptoms[]' id=$id class='symptom' value=$id><label for=$id>$symptomName</label></td>";
              }

              if ($i+3<count($symptomlist)){
                $id = $symptomlist[$i+3]['ID'];
                $symptomName = ucfirst($symptomlist[$i+3]['Name']);
                $row .= "<td width=300><input type='checkbox' name='symptoms[]' id=$id class='symptom' value=$id><label for=$id>$symptomName</label></td>";
              }
              
              echo "<tr> $row </tr>";
            }
          ?>
        </table>
      </div>
      <!-- <?php

          // $test = $Symptoms->diagnosisClient->loadDiagnosis([16], 'male', 2009);

          // var_dump($test);
      ?> -->
      <button id="searchBtn" type="button" class="btn btn-primary" > Submit </button>
    </form>

    
    <!-- <table id="resultsTable" class='table table-striped' border='1'>
        <thead class='thead-dark'>
            <tr>
                <th>Title</th>
                <th>ISBN 13</th>
                <th>Price</th>
                <th>Availability</th>
            </tr>
        </thead>
    </table> -->
  </div>


  <script>
    console.log(1);
    document.write('hi');
    
    // // $('#resultsTable').hide();
    // // // Helper function to display error message
    // // function showError(message) {
    // //     // Hide the table and button in the event of error
    // //     $('#resultsTable').hide();

    // //     // Display an error under the main container
    // //     $('#symptomchecker')
    // //         .append("<label>"+message+"</label>");
    // // }
    // // $("#searchBtn").submit(async (event) => {


    $('#searchBtn').click((event) => {  
    //Prevents screen from refreshing when submitting  
        console.log('hello');

        event.preventDefault();
        var yearofbirth = $('#yearofbirth').val();
        var gender = $('.gender').val();
        var symptom = [];
            $.each($("input[name='symptoms[]']:checked"), function(){
                symptom.push($(this).val());
            });
        // document.write(symptom);
        // function createCookie(name, value, days) {
        //   var expires;
        //   if (days) {
        //     var date = new Date();
        //     date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        //     expires = "; expires=" + date.toGMTString();
        //   }
        //   else {
        //     expires = "";
        //   }
        //   document.cookie = escape(name) + "=" + escape(value) + expires + "; path=/";
        // }
        
        // $(document).ready(function () {
        //   createCookie("yearofbirth", yearofbirth, "10");
        //   createCookie("gender", gender, "10");
        //   createCookie("symptom", symptom, "10");
        //   console.log(1);
        // });

        

        $.ajax({
          method: "POST",
          data: { "yearofbirth": yearofbirth, "gender": gender, "symptom": symptom }
        })
        
        try {
            const diagnosis = 
            <?php
                $getSymptom = $_POST['symptom'];
                var_dump($getSymptom);
                $getGender = $_POST['gender'];
                $getYr = $_POST['yearofbirth'];
                // $getSymptom = "<script>document.writeIn(symptom);</script>";
                // $getGender = "<script>document.writeIn(gender);</script>";
                // $getYr = "<script>document.writeIn(yearofbirth);</script>";
                return $getYr;
                return $Symptoms->diagnosisClient->loadDiagnosis($getSymptom, $getGender, $getYr);?>;
            console.log(diagnosis);
            // const response =
            // await fetch(
            //     serviceURL, { method: 'GET' }
            // );
            const data = diagnosis.json();
            // var books = data.books; //the arr is in data.books of the JSON data

            // array or array.length are falsy
            // if (response.ok) {
            //     console.log(data);
            //     // for loop to setup all table rows with obtained book data
            //     // var rows = "";
            //     //     eachRow =
            //     //         "<td>" + data.title + "</td>" +
            //     //         "<td>" + data.isbn13 + "</td>" +
            //     //         "<td>" + data.price + "</td>" +
            //     //         "<td>" + data.availability + "</td>";
            //     //     rows += "<tbody><tr>" + eachRow + "</tr></tbody>";
            //     // // add all the rows to the table
            //     // $('#booksTable').append(rows);
            //     // $('#booksTable').show();
            // } 
        } catch (error) {
            // Errors when calling the service; such as network error, 
            // service offline, etc
            showError
          ('There is a problem retrieving books data, please try again later.<br />'+error);
            
        } // error
    });

  </script>


</body>
</html>