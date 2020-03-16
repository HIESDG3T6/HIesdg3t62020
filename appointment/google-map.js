function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: {lat: 1.3521, lng: 103.8198}  // Singapore
    });
  
    var directionsService = new google.maps.DirectionsService;
    var directionsRenderer = new google.maps.DirectionsRenderer({
      draggable: true,
      map: map,
      panel: document.getElementById('right-panel')
    });
  
    directionsRenderer.addListener('directions_changed', function() {
      computeTotalDistance(directionsRenderer.getDirections());
    });
  
    displayRoute('redhill mrt, SG', 'lee kong chian business school, SG', directionsService,
        directionsRenderer);
  }
  
  function displayRoute(origin, destination, service, display) {
    service.route({
      origin: origin,
      destination: destination,
      // waypoints: [{location: 'Adelaide, SA'}, {location: 'Broken Hill, NSW'}],
      travelMode: 'TRANSIT',
      avoidTolls: true
    }, function(response, status) {
      if (status === 'OK') {
        display.setDirections(response);
      } else {
        alert('Could not display directions due to: ' + status);
      }
    });
  }
  
  function computeTotalDistance(result) {
    var total = 0;
    var myroute = result.routes[0];
    for (var i = 0; i < myroute.legs.length; i++) {
      total += myroute.legs[i].distance.value;
    }
    total = total / 1000;
    document.getElementById('total').innerHTML = total + ' km';
  }