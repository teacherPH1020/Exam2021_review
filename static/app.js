/*
Sergey Postnikov
teacher
39 years older
*/

// my first javascript

// <script> not needed

//alert("page is loaded");

var name;
name = "Sergey";

var age = 39;

console.log(name);
console.log("age");
console.log(age);


var blond = false;
console.log(blond);

var $carPrice = 2000;
console.log(typeof($carPrice));
$carPrice  = "3000"
console.log(typeof($carPrice));

var a=1; var A='one';
var b = a+A;
console.log(b);
console.log(typeof(b));

var model = "Toyota",
    color = "grey",
    year = 2003;

console.log("Car:"+model+' '+color+' '+year);

const pi = 3.14;

var say = 'It\'s ok!';

var minsk_population = 2.04e+6;
console.log(minsk_population);


var old = (age>60);
console.log("old?",old);

var data = undefined; // var data;
console.log(data, typeof(data));

var bookObj = {
        title : "World",
        pages : 245,
        author : "Marks Segan"
}
document.write(bookObj.title,"<br>", bookObj.author);

function sphere_vol (r){
    //return 3.14*4*r*r*r/3;
    return 3.14*4*Math.power(r,3)/3;
}

document.write("<br>Sphere volume r=3.5 <br>")
document.write(sphere_vol(3))

var secret;

(function () {secret="<br>I can fly<br>";})()
document.write(secret)

function tell_secret(){
    let secret = "<br>I can cure cancer<br>";
    return secret;
}
document.write(tell_secret());

var n = 3;

document.write(n==3);
document.write(n=='3');
document.write(n!='3');
document.write(n==='3');
document.write(n!=='3');
document.write('<hr>');
document.write(!(n===3));

var v;
if (age>16) {
    v='adult';
}
else if (age<16){
    v='child';
}
else {
    v='almost';
}
document.write(v);

document.write(name == 'Sergey'? 'I know you':"Who are you?");

var houseObj = new Object();
houseObj.price = "100000$"
houseObj.size = 20
houseObj.neww = true
houseObj.color = "blue"

var prop = "neww"
document.write("<hr>",houseObj[prop]);

for (p in houseObj){
    document.write("<br>",p,"=",houseObj[p]);
}
delete houseObj.color;
document.write("<hr>",JSON.stringify(houseObj));

document.getElementById("forJS").innerHTML="New content";

var arr = [0,1,2,3,4,5];
document.write("<hr>", arr.toString())

console.log(Math.PI);