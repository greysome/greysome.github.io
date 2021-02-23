var heads = 0;
var seq = [];
var board, slide_a, slide_b, graph_pr, graph_post;

function update_text() {
    var str = "";
    for (var i = 0; i < seq.length; i++) {
        str += seq[i] ? "H" : "T";
    }
    document.getElementById("txt_seq").innerHTML = str;
}

function update_posterior() {
    board.removeObject(graph_post);
    graph_post = board.create('functiongraph', [
	function(x) {
	    return beta(x, slide_a.Value() + heads, slide_b.Value() + (seq.length-heads));
	}, 0, 1
    ], {strokeColor: 'red'});
}

document.getElementById("btn_heads").onclick = function() {
    seq.push(1);
    heads += 1;
    update_text();
    update_posterior();
}

document.getElementById("btn_tails").onclick = function() {
    seq.push(0);
    update_text();
    update_posterior();
}

document.getElementById("btn_reset").onclick = function() {
    seq = [];
    heads = 0;
    update_text();
    board.removeObject(graph_post);
}

// Copied from Wikipedia (Lanczos approximation)
const p = [676.5203681218851, -1259.1392167224028, 771.32342877765313,
	   -176.61502916214059, 12.507343278686905, -0.13857109526572012,
	   9.9843695780195716e-6, 1.5056327351493116e-7];
function gamma(z) {
    var y;
    if (z < 0.5) {
        // Reflection formula
        y = Math.PI / (Math.sin(Math.PI * z) * gamma(1 - z));
    }
    else {
        z -= 1;
        var x = 0.99999999999980993;
	for (var i = 0; i < p.length; i++) {
            x += p[i] / (z + i + 1);
	}
        var t = z + p.length - 0.5;
        y = Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
    }
    return y;
}
    
function beta(x,a,b) {
    return gamma(a+b) * Math.pow(x, a-1) * Math.pow(1-x, b-1) / (gamma(a) * gamma(b));
}

board = JXG.JSXGraph.initBoard('jxgbox', { 
    boundingbox: [-0.1, 5.4, 1.1, -0.4],
    axis: true,
    showCopyright: false,
    showNavigation: false
});
slide_a = board.create('slider', [[0.6,5], [0.9,5], [0,10,10]], {name:'a'});
slide_b = board.create('slider', [[0.6,4.5], [0.9,4.5], [0,10,10]], {name:'b'});
graph_pr = board.create('functiongraph', [
    function(x) {
	return beta(x, slide_a.Value(), slide_b.Value());
    }, 0, 1
]);
