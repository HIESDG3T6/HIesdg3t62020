<!--
author: W3layouts
author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Patient Panel </title>
		<!-- for-mobile-apps -->
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		
			<script>
				addEventListener("load", function () {
					setTimeout(hideURLbar, 0);
				}, false);
		
				function hideURLbar() {
					window.scrollTo(0, 1);
				}
			</script>
			
			<!-- css files -->
			<link href="../css/css_slider.css" type="text/css" rel="stylesheet" media="all"><!-- slider css -->
			<link href="../css/bootstrap.css" rel='stylesheet' type='text/css' /><!-- bootstrap css -->
			<link href="../css/style.css" rel='stylesheet' type='text/css' /><!-- custom css -->
			
			<!-- //css files -->
			
			<!-- google fonts -->
			<link href="//fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i&amp;subset=cyrillic,cyrillic-ext,greek,greek-ext,latin-ext,vietnamese" rel="stylesheet">
			<link href="//fonts.googleapis.com/css?family=Dosis:200,300,400,500,600,700,800&amp;subset=latin-ext" rel="stylesheet">
			<!-- //google fonts -->
			
			<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
			<script 
				src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
				<script src="js/jquerysession.js"></script>
            	<script src="js/site.js"></script>
				<script
				src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"
				integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut"
				crossorigin="anonymous"></script>

				<!-- session -->
				<script>
					if ($.session.get('userid') == null){
						window.location.replace("/esd/patient/login.html");
					}

					var name = $.session.get('name');
					// console.log($.session.get('userid'));
				</script>
		</head>
<body>

<!-- top header -->
<div class="header-top">
	<div class="container">
		<div class="row">
			<div class="col-sm-6">
				<ul class="d-lg-flex header-w3_pvt">
					<li class="mr-lg-3">
						<p id="patientNameHeading"> Welcome! Patient </p>
						
					</li>
				</ul>
			</div>
			<div class="col-sm-6 header-right-w3_pvt">
				<ul class="d-lg-flex header-w3_pvt justify-content-lg-end">
					<li class="mr-lg-3"><a class="user" href="logout.html">Logout</a></li>
				</ul>
			</div>
		</div>
	</div>
	<script>
		$('#patientNameHeading').append(name);	
	</script>
</div>
<!-- //top header -->

<!-- //header -->
<header class="py-3">
	<div class="container">
			<div id="logo">
				<h1> <a href="index.html"><span class="fa fa-stethoscope" aria-hidden="true"></span> Health Insurance </a></h1>
			</div>
		<!-- nav -->
		<nav class="d-lg-flex">

			<label for="drop" class="toggle"><span class="fa fa-bars"></span></label>
			<input type="checkbox" id="drop" />
			<ul class="menu mt-2 ml-auto">
				<li class=""><a href="precheck.html">Symptoms Checker</a></li>
				<li class=""><a href="search.php">Search Clinics </a></li>
				<li class=""><a href="patient_history.html">Medical History</a></li>
				<li class=""><a href="account.html">Appointment Details</a></li>
			</ul>
			<div class="login-icon ml-2">
				<a class="user" href="appointment.html"> Book Appointment Now</a>
			</div>
		</nav>
		<div class="clear"></div>
		<!-- //nav -->
</header>
<!-- //header -->

<br><br>
<!-- contact -->
<section class="mail pt-lg-5 pt-4">
	<div class="container pt-lg-5">
		<h2 class="heading text-center mb-sm-5 mb-4">Search for a Clinic</h2>
		<div class="row agileinfo_mail_grids">
			<div class="col-lg-8 agileinfo_mail_grid_right">
				<form action="#" method="post">
					<div class="row">
						<div class="col-md-6 wthree_contact_left_grid pr-md-0">
							<div class="form-group">
								<input type="text" name="name" id="clinicName" class="form-control" placeholder="Clinic Name" >
							</div>
						</div>
						<div class="col-md-6 wthree_contact_left_grid">
							<div class="form-group">
								<select name="specialty" class="form-control" id="specialty">
									<option value="">Select a Specialty</option>
								</select>							
							</div>
						</div>
						<div class="col-lg-4 col-md-6 mt-lg-0 mt-4">
							<div class="form-group">
								<select name="groupedlocation" class="form-control" id="location">
									<option value="">Select an Area</option>
								</select>								
							</div>
						</div>
						<div class="col-md-12">
							<div class="submit-buttons">
								<button type="submit" id="searchBtn" class="btn">Submit</button>
							</div>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>
<hr>
	<table id="clinics" class='table' border='1'>
	</table>

	<table id="clinicsSearch" class='table' border='1'>
	</table>
</section>

	<div id="results"></div>
	
	<?php
		$passedSpec = "";
		if (isset($_GET['specialty'])){
			$passedSpec = $_GET['specialty'];
		}
	?>
		
	<script>
		$('#clinics').hide();		
		function showError(message) {
			$('#clinics').hide();
	
			$('#main-container').append("<label>"+message+"</label>");
		}

        $(document).ready(async() => {  
			var passedspec = "<?php echo $passedSpec; ?>";
			// console.log(passedspec);

			var serviceURL = "http://localhost:5111/clinic";

            try {
                const response =
                await fetch(
                   serviceURL, { method: 'GET' }
                );
                const data = await response.json();

                if (response.ok) {
                    // console.log(data);
					var rows = "";
					var specarr = [];
					var locarr = [];
					$.each(data, function(index, value){
						$.each(value, function(index, value2){
							// console.log(value2);
							eachRow =
								"<td><h6>" + value2.clinicName + "</h6><br>" +
								"Specialty: " + value2.specialty + "<br>" +
								"Address: " + value2.address + "<br>" +
								"S(" + value2.postalCode + ")<br>" +
								"Contact: " + value2.contactNumber + "<br>" +
								"Opening Hours: " + value2.opening + "<br>" +
								"<td align='center'><iframe src='../clinicsearch/distance.php?location=" + value2.address + "'></iframe><br><a href='appointment.html?clinic=" + value2.clinicName +"&postalcode=" +value2.postalCode + "'>Book Appointment</a></td>";
							rows += "<tbody><tr>" + eachRow + "</tr></tbody>";
							if (jQuery.inArray(value2.specialty, specarr) == -1){
								specarr.push(value2.specialty);
							}
							// console.log(specarr);
							if (jQuery.inArray(value2.groupedLocation, locarr) == -1){
								locarr.push(value2.groupedLocation);
							}
							// console.log(value2.groupedLocation);
						});
					});
					// add all the rows to the table
					// console.log(rows);
					if (passedspec == "") {
						$('#clinics').append(rows);
					}
					else{
						var serviceURL = "http://localhost:5111/clinic/spec" + "/" + passedspec;
						const anotherresponse =
						await fetch(
							serviceURL, { method: 'GET' }
						);
						const data = await anotherresponse.json();
						// var books = data.books; //the arr is in data.books of the JSON data
						// console.log(data);

						// array or array.length are falsy
						if (anotherresponse.ok) {
							// console.log(data);
							// for loop to setup all table rows with obtained book data
							var rows = "";
							$.each(data, function(index, value){
									// console.log(value2);
								eachRow =
									"<td><h6>" + value.clinicName + "</h6><br>" +
									"Specialty: " + value.specialty + "<br>" +
									"Address: " + value.address + "<br>" +
									"S(" + value.postalCode + ")<br>" +
									"Contact: " + value.contactNumber + "<br>" +
									"Opening Hours: " + value.opening + "<br>" +
									"<td align='center'><iframe src='../clinicsearch/distance.php?location=" + value.address + "'></iframe><br><a href='appointment.html?clinic=" + value.clinicName +"&postalcode=" +value.postalCode + "'>Book Appointment</a></td>";
								rows += "<tbody><tr>" + eachRow + "</tr></tbody>";

								});
								// add all the rows to the table
								$('#clinics').append(rows);
							}}
					$('#clinics').show();

					var specrows = "";
					specarr.sort();
					$.each(specarr, function(index, value){
						specrows += "<option value='" + value + "'>" + value + "</option>";
					});
					// console.log(specrows);
					$('#specialty').append(specrows);

					var locrows = "";
					locarr.sort();
					$.each(locarr, function(index, value){
						locrows += "<option value='" + value + "'>" + value + "</option>";
					});
					// console.log(locrows);
					$('#location').append(locrows);
                } 
            } catch (error) {
                showError
              ('There is a problem retrieving clinic data, please try again later.<br />'+error);
               
            } 
		});
		
		$('#searchBtn').click(async(event) => {  
        //Prevents screen from refreshing when submitting  
            event.preventDefault();
			$('#clinics').hide();

			if ($('#clinicName').val()!== "" && $('#specialty').val()!== "" && $('#location').val()!== ""){
				var clinicName = $('#clinicName').val();
				var specialty = $('#specialty').val();
				var groupedlocation = $('#location').val();
				var serviceURL = "http://localhost:5111/clinic" + "/" + clinicName + "/" + groupedlocation + "/" + specialty;
			}
			else if ($('#clinicName').val()!== "" && $('#location').val()!== ""){
				var clinicName = $('#clinicName').val();
				var groupedlocation = $('#location').val();
				var serviceURL = "http://localhost:5111/clinic/nameloc" + "/" + clinicName + "/" + groupedlocation;
			}
			else if ($('#clinicName').val()!== "" && $('#specialty').val()!== ""){
				var clinicName = $('#clinicName').val();
				var specialty = $('#specialty').val();
				var serviceURL = "http://localhost:5111/clinic/namespec" + "/" + clinicName + "/" + specialty;
			}
			else if ($('#specialty').val()!== "" && $('#location').val()!== ""){
				var specialty = $('#specialty').val();
				var groupedlocation = $('#location').val();
				var serviceURL = "http://localhost:5111/clinic/specloc" + "/" + groupedlocation + "/" + specialty;
			}
			else if ($('#clinicName').val()!== ""){
				var clinicName = $('#clinicName').val();
				var serviceURL = "http://localhost:5111/clinic" + "/" + clinicName;
			}
			else if ($('#specialty').val()!== ""){
				var specialty = $('#specialty').val();
				var serviceURL = "http://localhost:5111/clinic/spec" + "/" + specialty;
			}
			else if ($('#location').val()!== ""){
				var groupedlocation = $('#location').val();
				var serviceURL = "http://localhost:5111/clinic/loc" + "/" + groupedlocation;
			}
			else{
				alert('Please Fill in a Field');
			}
			
            try {
                const response =
                await fetch(
                   serviceURL, { method: 'GET' }
                );
                const data = await response.json();
				// console.log(data);

				// array or array.length are falsy
                if (response.ok) {
                    // console.log(data);
					var rows = "";
					$.each(data, function(index, value){
							// console.log(value2);
						eachRow =
							"<td><h6>" + value.clinicName + "</h6><br>" +
							"Specialty: " + value.specialty + "<br>" +
							"Address: " + value.address + "<br>" +
							"S(" + value.postalCode + ")<br>" +
							"Contact: " + value.contactNumber + "<br>" +
							"Opening Hours: " + value.opening + "<br>" +
							"<td align='center'><iframe src='../clinicsearch/distance.php?location=" + value.address + "'></iframe><br><a href='appointment.html?clinic=" + value.clinicName +"&postalcode=" +value.postalCode + "'>Book Appointment</a></td>";
						rows += "<tbody><tr>" + eachRow + "</tr></tbody>";

					});
					// add all the rows to the table
					// console.log(rows);
					$('#clinicsSearch').empty().append(rows);
					$('#clinicsSearch').show();
				} 
				else{
					$('#clinicsSearch').empty().append('No Clinics Found');
				}
            } catch (error) {
                showError
              ('There is a problem retrieving clinic data, please try again later.<br />'+error);
               
            } // error
		});	

	</script>

	<!-- Map -->
	<!-- <div class="map mt-5">
		<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d50996.31320435244!2d-122.06676498187694!3d36.97949802442312!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808e441b7c36d549%3A0x52ca104b2ad7f985!2sSanta+Cruz%2C+CA%2C+USA!5e0!3m2!1sen!2sin!4v1469096018666"
			style="border:0"></iframe>
	</div> -->

<!-- copyright -->
<div class="copyright">
	<div class="container py-4">
		<div class=" text-center">
			<p>© 2020 Health Insurance Inc. All Rights Reserved </a> </p>
		</div>
	</div>
</div>
<!-- //copyright -->
		
<!-- move top -->
<div class="move-top text-right">
	<a href="#home" class="move-top"> 
		<span class="fa fa-angle-up  mb-3" aria-hidden="true"></span>
	</a>
</div>
<!-- move top -->



</body>
</html>