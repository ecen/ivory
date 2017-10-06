ids = [].slice.call(document.getElementsByClassName("app")).map(function(o) {return o.getElementsByTagName("td")[0].getElementsByTagName("a")[0].innerHTML});
names = [].slice.call(document.getElementsByClassName("app")).map(function(o) {return o.getElementsByTagName("td")[1].innerHTML});
pos = [].slice.call(document.getElementsByClassName("app")).map(function(o) {return parseInt(o.getElementsByTagName("td")[2].innerHTML.replace(/,/g,''))});
neg = [].slice.call(document.getElementsByClassName("app")).map(function(o) {return parseInt(o.getElementsByTagName("td")[3].innerHTML.replace(/,/g,''))});
total = (function() { var list = []; for (var i = 0; i < ids.length; i++) { list[i] = pos[i] + neg[i];} return list; })();

var viable = 0;
for (var i = 0; i < ids.length; i++) {
	if (total[i] >= 100) {
		viable++;
		console.log(viable + " " + ids[i] + " " + names[i] + " " + pos[i]);
    }
}