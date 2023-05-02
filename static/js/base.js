$(function(){ 

  $("button").click(function(){
    $(".modal").fadeIn();
  });

});
//  center 부분 위도 경도 위치 설정바람
// window.initMap = function () {
// // 마커 기능 각 시/도 로 변경 / 위도 경도 변경 필수
//   const malls = [
//     { label: "C", name: "코엑스몰", lat: 37.5115557, lng: 127.0595261 },
//     { label: "G", name: "고투몰", lat: 37.5062379, lng: 127.0050378 },
//     { label: "D", name: "동대문시장", lat: 37.566596, lng: 127.007702 },
//     { label: "I", name: "IFC몰", lat: 37.5251644, lng: 126.9255491 },
//     { label: "L", name: "롯데월드타워몰", lat: 37.5125585, lng: 127.1025353 },
//     { label: "M", name: "명동지하상가", lat: 37.563692, lng: 126.9822107 },
//     { label: "T", name: "타임스퀘어", lat: 37.5173108, lng: 126.9033793 }
//   ];

//   const bounds = new google.maps.LatLngBounds();
//   const infoWindow = new google.maps.InfoWindow();

//   malls.forEach(({ label, name, lat, lng }) => {
//     const marker = new google.maps.Marker({
//       position: { lat, lng },
//       label,
//       map
//     });
//     bounds.extend(marker.position);

//     marker.addListener("click", () => {
//       map.panTo(marker.position);
//       infoWindow.setContent(name);
//       infoWindow.open({
//         anchor: marker,
//         map
//       });
//     });
//   });

//   map.fitBounds(bounds);
// };
