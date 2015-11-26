/**
 * Created by dermersean on 26/11/2015.
 */

$('#suggestions').click(function(){
    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});

$('#submitSearch').click(function()
{
    var searchWord = $('#searchFood').val();
    $.post('/commitSearch',searchWord);
});

$("#img1").hover(function(){},function(){suggestions()});

function suggestions()
{
    document.getElementById("img1").style.display = "none";
    document.getElementById("img5").style.display = "inline";
    //document.getElementById("here").innerHTML=output;
}
