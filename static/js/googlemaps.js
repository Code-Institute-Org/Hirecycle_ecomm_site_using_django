/**
 * Created by nakita on 28/03/2017.
 */
function initMap() {
    var uluru = {lat: 53.338963, lng: -6.2590447};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: uluru
    });
    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}

// SCRIPTS
//     <!-- googlemaps custom script and API call -->
//     <script src= "{% static "js/googlemaps.js" %}"></script>
//     <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDTZgAJCOUegjDDnQKCNGFTUrxX5QY9-Qc&callback=initMap">
//     </script>