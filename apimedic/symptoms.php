<?php
    // require_once 'config.py';
    // require_once 'PriaidDiagnosisClient.py';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
                        
    <script src="js/hmac-md5.js"></script>                        
    <script src="js/enc-base64-min.js"></script>
    <script>
        var uri = "https://authservice.priaid.ch/login";
        var secret_key = "mysecretkey";
        var computedHash = CryptoJS.HmacMD5(uri, secret_key);
        var computedHashString = computedHash.toString(CryptoJS.enc.Base64);     
    </script>
</head>
<body>
    
    Select Affected Body Location:
    <select id="locality-dropdown" name="locality">
    </select><br><br>

    Select Symptoms:
    <select id="symptoms-dropdown" name="symptoms">
    </select>

    <script>
        var token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imh1aWZlbi5vbmcuMjAxOEBzbXUuZWR1LnNnIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI2NjIyIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMjAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6Ijk5OTk5OTk5OSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IlByZW1pdW0iLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDIwLTAzLTEzIiwiaXNzIjoiaHR0cHM6Ly9zYW5kYm94LWF1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1ODQyOTMyNDUsIm5iZiI6MTU4NDI4NjA0NX0.4HDwVs0OWCqM0dzEhvvlI92BEOj3m-qYFknRnae2chE';

// body location
        var url = 'https://sandbox-healthservice.priaid.ch/body/locations?token=' + token + '&language=en-gb';
        obj = { table: "bodylocation", limit: 20 };
        dbParam = JSON.stringify(obj);
        xmlhttp = new XMLHttpRequest();
        txt = '';
        xmlhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            var myObj = JSON.parse(this.responseText);
            console.log(myObj);
            txt += "<select>"
            for (x in myObj) {
              txt += "<option>" + myObj[x].Name;
            }
            txt += "</select>"
            document.getElementById("locality-dropdown").innerHTML = txt;
          }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp.send("x=" + dbParam);

        // console.log(myObj);


// symptoms
        var url2 = 'https://sandbox-healthservice.priaid.ch/symptoms?token=' + token + '&language=en-gb';
        obj2 = { table: "symptoms", limit: 20 };
        dbParam2 = JSON.stringify(obj2);
        xmlhttp2 = new XMLHttpRequest();
        txt = '';
        xmlhttp2.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            var myObj2 = JSON.parse(this.responseText);
            console.log(myObj2);
            txt += "<select>"
            for (x in myObj2) {
              txt += "<option>" + myObj2[x].Name;
            }
            txt += "</select>"
            document.getElementById("symptoms-dropdown").innerHTML = txt;
          }
        }
        xmlhttp2.open("GET", url2, true);
        xmlhttp2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp2.send("x=" + dbParam2);

    </script>
    
</body>
</html>


