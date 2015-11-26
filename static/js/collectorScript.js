/**
 * Created by Erez Levanon on 25/11/2015.
 */
var curFoodId = 1;
var curMovieId = 2;
reloadPage();

function reloadPage()
{
    $.get('/getInfo', function(data){
        alert(data);
        alert(data["recipeId"]);
        curFoodId = data["recipeId"];
        curMovieId = data["movieId"];
        document.getElementById("movieName").innerHTML= data["movieName"];
        document.getElementById("foodName").innerHTML= data["recipeName"];
        document.getElementById("moviePic").src = data["movieImage"];
        document.getElementById("foodPic").src = data["recipeImage"];
    });
}

function sendRate(rate)
{
    var data = {movieId:curMovieId, foodId:curFoodId, rate:rate};
    $.post('/postRate', data, reloadPage());
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