/**
 * Created by Erez Levanon on 25/11/2015.
 */
var foodId = 1;
var movieId = 2;
reloadPage();

function reloadPage()
{
    var info = getInfo();
    document.getElementById("movieName").innerHTML="HollyMolly";
    document.getElementById("foodName").innerHTML='guacamole';
    document.getElementById("moviePic").src = "https://static.pexels.com/photos/7976/pexels-photo.jpg";
    document.getElementById("foodPic").src = "https://static.pexels.com/photos/7976/pexels-photo.jpg";
}

function sendRate(rate)
{
    //var data = '{ "movieId":' + movieId + ', "foodId":' + foodId + ',"rate":' + rate + '}';
    var data = {"movieId":movieId, "foodId":foodId, "rate":rate};
    $.post('/postRate', data, reloadPage());
}

function getInfo()
{
    var info = $.get('/getInfo');
    foodId = info.movieId;
    movieId = info.movieId;
}




$('#rate1').on('click', function(e) {
    sendRate(1);
});

$('#rate2').on('click', function(e) {
    sendRate(2);
});
$('#rate3').on('click', function(e) {
    sendRate(3);
});
$('#rate4').on('click', function(e) {
    sendRate(4);
});
$('#rate5').on('click', function(e) {
    sendRate(5);
});