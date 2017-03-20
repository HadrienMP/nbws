$(function () {
    $("#refresh").click(update);
});
function update() {
    $('.line').each(function () {
        updateLine($(this));
    });
}
function updateLine($line) {
    var key = $line.find(".description").text();
    $.get("line/" + key, function (times) {
        for (var i = 0; i < times.length; i++) {
            var $section = $line.find("section").eq(i);
            console.log(times[i][0] + ', ' + times[i][1]);
            $section.find(".destination").text(times[i][0]);
            $section.find(".minutes").text(times[i][1]);
            $section.find(".time").text(times[i][2]);
        }
    });
}