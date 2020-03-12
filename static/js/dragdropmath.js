var time_left = 0;
var time_dir = 1;
var timer_interval = false;

var time_taken = 0;
var time_taken_interval = false;

var sprite_number = 0;

var operator_symbol = [];
operator_symbol['addition'] = '+';
operator_symbol['division'] = '/';
operator_symbol['multiplication'] = 'x';
operator_symbol['subtraction'] = '-';

var already_guessed = false;

var mousex = false;
var mousey = false;
var moving_sprite_number = -1;
var moving_sprite_element_id = false;
var moving_sprite_element_offset_x = false;
var moving_sprite_element_offset_y = false;
var moving_sprite_element_start_x = false;
var moving_sprite_element_start_y = false;

var zoom = 1;	//1.14;

var line_start_x = false;
var line_start_y = false
var line_end_x = false
var line_end_y = false;

var score = 0;
var question_number = 0;
var max_questions = 10;

var questions_array = [];
var answers_array = [];

var custom_questions = [];
var custom_question_number = 0;

var game_type = 'addition';
var teachers_game_type = false;

var use_remainder = true;

var addition_row_array = [4, 4, 4, 4];
var addition_row_total = 2;

var multiplication_row_array = [4, 4, 4, 4];
var multiplication_row_total = 2;

var division_row_array = [4, 4, 4, 4];
var division_row_total = 2;

var subtraction_row_array = [4, 4, 4, 4];
var subtraction_row_total = 2;

var all_digits = '1234';

var correct_answer = false;
var all_numbers = [];

var images_preloaded = new Array();
var load_progress = 0;
var loaded = new Array();
var timer_id;
var total_loaded;
var sounds = [];
var sounds_loaded = [];
var sound_files = ['correct', 'incorrect', 'music'];
var audio_on = true;
var transform_property = false;

var IE = false;
//@cc_on IE = true;

//if (typeof document.oncontextmenu != 'undefined') document.oncontextmenu = ce; else document.onclick = nrc;
if (typeof document.onselectstart != 'undefined') document.onselectstart = ce;
if (typeof document.ondragstart != 'undefined') document.ondragstart = ce;

//if (typeof document.ontouchmove != 'undefined') document.ontouchmove = ce;

function init()
{
document.getElementById('main_div').style.display='block';

transform_property = get_transform_property(document.getElementById('main_div'));

load_audio();

document.onmousemove = m;
document.ontouchmove = m;
document.onmouseup = stop_moving_sprite;
document.ontouchend = stop_moving_sprite;

document.getElementById('game_inner').onmousedown = start_line;
document.getElementById('game_inner').ontouchstart = start_line;

if (teacher_mode)
	{
	preload_problems();
	//game_type = 'teachers';
	document.getElementById('frontpage_div').style.display = 'none';
	document.getElementById('options_div_teachers').style.display = 'block';
	//game_menu();
	return;
	}

play_sound(2);

if (preload_questions)
	{
	custom_questions = preload_questions.split('|');
	game_type = 'teachers';
	}

if (preload_checkboxes)
	{
	reload_checkboxes();
	}

//document.onmouseup = stop_line;
}

function reload_checkboxes()
{
var psv_pointer = 0;
var checkboxes = preload_checkboxes.split('|');

for (var i = 1; i <= 4; i ++)
	{
	document.getElementById('addition_mults_checkbox_' + i + '_0').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	document.getElementById('addition_mults_checkbox_' + i + '_1').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	}

for (var i = 1; i <= 2; i ++)
	{
	document.getElementById('multiplication_mults_checkbox_' + i + '_0').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	document.getElementById('multiplication_mults_checkbox_' + i + '_1').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	document.getElementById('subtraction_mults_checkbox_' + i + '_0').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	document.getElementById('subtraction_mults_checkbox_' + i + '_1').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	document.getElementById('division_mults_checkbox_' + i + '_0').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	document.getElementById('division_mults_checkbox_' + i + '_1').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
	}

addition_row_total = checkboxes[psv_pointer ++];
addition_row_array = checkboxes[psv_pointer ++].split(',');
multiplication_row_total = checkboxes[psv_pointer ++];
multiplication_row_array = checkboxes[psv_pointer ++].split(',');
subtraction_row_total = checkboxes[psv_pointer ++];
subtraction_row_array = checkboxes[psv_pointer ++].split(',');
division_row_total = checkboxes[psv_pointer ++];
division_row_array = checkboxes[psv_pointer ++].split(',');
document.getElementById('vary_checkbox').checked = checkboxes[psv_pointer ++] == '1' ? true : false;
game_type = checkboxes[psv_pointer ++];
}

function show_teacher_options()
{
document.getElementById('options_div_teachers').style.display = 'block';
}

function main_menu()
{
use_remainder = true;
max_questions = 10;
question_number = 0;
custom_questions = [];
document.getElementById('problem_list_div').innerHTML = '';
game_type = 'addition';
document.getElementById('options_div_teachers').style.display='none';
document.getElementById('frontpage_div').style.display='none';
document.getElementById('menu_div').style.display = 'block';
}

function show_info()
{
document.getElementById('frontpage_div').style.display = 'none';
document.getElementById('info_div').style.display = 'block';
}

function show_frontpage()
{
document.getElementById('frontpage_div').style.display = 'block';
document.getElementById('info_div').style.display = 'none';
document.getElementById('game_over_div').style.display = 'none';
}

function game_options(this_game_type, clicked_element)
{
for (var i = 0; i < 4; i ++)
	{
	document.getElementById('option_' + i).style.border = 'none';
	}

clicked_element.style.border = '2px solid #ffff00';

game_type = this_game_type;
}

function game_menu()
{
document.getElementById('frontpage_div').style.display = 'none';
document.getElementById('menu_div').style.display = 'none';

//if (game_type != 'teachers')
	{
	document.getElementById('options_div').style.display = 'block';
	use_remainder = true;
	}

document.getElementById('option_selected_image').innerHTML = game_type;

document.getElementById('options_div_addition').style.display = 'none';
document.getElementById('options_div_subtraction').style.display = 'none';
document.getElementById('options_div_multiplication').style.display = 'none';
document.getElementById('options_div_division').style.display = 'none';
document.getElementById('options_div_teachers').style.display = 'none';

document.getElementById('options_div_' + game_type).style.display = 'block';
}

function restart_teachers()
{
document.getElementById('frontpage_div').style.display = 'none';
document.getElementById('options_div').style.display = 'block';
setTimeout(teacher_name_entry, 500);
}

function teacher_name_entry()
{
document.getElementById('frontpage_div').style.display = 'none';
document.getElementById('options_div').style.display = 'block';
document.getElementById('options_div_teachers').style.display = 'none';
document.getElementById('options_bottom').style.display = 'none';
}

function restart()
{
reset();
document.getElementById('game_div').style.display = 'none';
document.getElementById('frontpage_div').style.display = 'block';

if (game_type != 'teachers') setTimeout(main_menu, 2000); else setTimeout(restart_teachers, 2000);
}

function create()
{
document.getElementById('frontpage_div').style.display = 'none';
document.getElementById('options_div_teachers').style.display = 'block';
}

function start_game()
{
if (teacher_mode)
	{
	var checkbox_psv = '';

	for (var i = 1; i <= 4; i ++)
		{
		checkbox_psv += (document.getElementById('addition_mults_checkbox_' + i + '_0').checked ? '1' : '0') + '|' + (document.getElementById('addition_mults_checkbox_' + i + '_1').checked ? '1' : '0') + '|';
		}

	for (var i = 1; i <= 2; i ++)
		{
		checkbox_psv += (document.getElementById('multiplication_mults_checkbox_' + i + '_0').checked ? '1' : '0') + '|' + (document.getElementById('multiplication_mults_checkbox_' + i + '_1').checked ? '1' : '0') + '|';
		checkbox_psv += (document.getElementById('subtraction_mults_checkbox_' + i + '_0').checked ? '1' : '0') + '|' + (document.getElementById('subtraction_mults_checkbox_' + i + '_1').checked ? '1' : '0') + '|';
		checkbox_psv += (document.getElementById('division_mults_checkbox_' + i + '_0').checked ? '1' : '0') + '|' + (document.getElementById('division_mults_checkbox_' + i + '_1').checked ? '1' : '0') + '|';
		}

	checkbox_psv += addition_row_total + '|' + addition_row_array.join(',') + '|' + multiplication_row_total + '|' + multiplication_row_array.join(',') + '|' + subtraction_row_total + '|' + subtraction_row_array.join(',') + '|' + division_row_total + '|' + division_row_array.join(',') + '|' + (document.getElementById('vary_checkbox').checked ? '1' : '0') + '|' + game_type;

	return;
	}

score = 0;
question_number = 0;

time_taken = 0;
time_taken_interval = setInterval('time_taken++', 1000);

questions_array = [];
answers_array = [];

document.getElementById('name_div').innerHTML = document.getElementById('username').value;

document.getElementById('frontpage_div').style.display = 'none';
document.getElementById('options_div').style.display = 'none';
document.getElementById('game_div').style.display = 'block';

display_game_area();
}

function display_game_area()
{
document.getElementById('menu_div').style.display = 'none';
document.getElementById('options_div').style.display = 'none';
document.getElementById('game_div').style.display = 'block';

teachers_game_type = false;

if (game_type != 'teachers') show_next_question(); else show_next_question_teachers();
}

function use_remainder_set(new_value, highlight_element)
{
use_remainder = new_value;

//document.getElementById('remainder_highlight').style.left = highlight_element.offsetLeft + 'px';
}

function skip_question()
{
question_number --;
show_next_question();
}

function setCharAt(str, index,chr)
{
if(index > str.length-1) return str;
return str.substr(0,index) + chr + str.substr(index+1);
}

function cancel_checkbox(clicked_element)
{
var other_checkbox = clicked_element.id;
other_checkbox = setCharAt(other_checkbox, other_checkbox.length - 1, clicked_element.id.substr(-1) == '0' ? '1' : '0');
document.getElementById(other_checkbox).checked = false;
}

function get_number(total_digits, i)
{
var this_number = Math.floor(Math.random() * (9 * '1000'.substr(0, total_digits)) + (parseInt('1000'.substr(0, total_digits))));

//if (document.getElementById(game_type + '_mults_' + (i + 1)).style.display != 'none')
	{
	if (document.getElementById(game_type + '_mults_checkbox_' + (i + 1) + '_0').checked) this_number = total_digits == 2 ? 10 : 100;
	if (document.getElementById(game_type + '_mults_checkbox_' + (i + 1) + '_1').checked) this_number = (Math.floor(Math.random() * 8) + 1) * (total_digits == 2 ? 10 : 100);
	}

//console.log(document.getElementById(game_type + '_mults_checkbox_' + (i + 1) + '_1').checked + ' ' + game_type + '_mults_checkbox_' + (i + 1) + '_0');

return this_number;
}

function show_next_question()
{
$('.remainder_input').hide();

if (game_type == 'teachers') return show_next_question_teachers();

reset();

question_number ++;

if (question_number > max_questions)
	{
	document.getElementById('result_overlay_div').innerHTML += '<img src="images/popup_scores_button.png" style="position:absolute;top:150px;left:0px;"><div id="final_result" style="position:absolute;top:8px;left:8px;width:98%;height:98%;text-align:center;font-size:42px;"><br>You Scored<br><div style="color:#ff0000;">' + ((100 / max_questions) * score) + '%</div><br><img src="images/ok_button.png" style="cursor:pointer;width:70px;" onclick="restart();">';
	return;
	}

document.getElementById('result_overlay_div').style.display = 'none';
document.getElementById('problem_div').innerHTML = question_number + '/' + max_questions;
document.getElementById('score_div').innerHTML = parseInt((100 / max_questions) * Math.floor(score)) + '%';
document.getElementById('result_div').value = '';
document.getElementById('result_int_div').value = '';
document.getElementById('result_rem_div').value = '';

var game_contents = '';

correct_answer = 0;
all_numbers = [];

already_guessed = false;

if (game_type == 'addition')
	{
	game_contents = '<div style="margin-left:35px;text-align:right;width:200px;">';

	for (var i = 0; i < addition_row_total; i ++)
		{
		var this_number = get_number(addition_row_array[i], i);

		correct_answer += this_number;

		all_numbers.push(this_number);

		if (i == addition_row_total - 1) game_contents += '+<span style="background-image:url(images/underline.png);">';

		game_contents += pad(this_number, 4, i) + '<br>';
		}

	game_contents += '</span>';
	}

if (game_type == 'multiplication')
	{
	game_contents = '<div style="margin-left:0px;text-align:right;width:280px;">';

	for (var i = 0; i < multiplication_row_total; i ++)
		{
		var this_number = get_number(multiplication_row_array[i], i);

		all_numbers.push(this_number);

		if (i == 0) correct_answer = this_number; else correct_answer *= this_number;

		if (i == multiplication_row_total - 1) game_contents += 'x<span style="background-image:url(images/underline.png);">';

		game_contents += pad(this_number, 4, i) + '<br>';
		}

	game_contents += '</span>';
	}

if (game_type == 'subtraction')
	{
	game_contents = '<div style="margin-left:35px;text-align:right;width:200px;">';

	//var numbers = [Math.floor(Math.random() * (9 * '1000'.substr(0, subtraction_row_array[0])) + (parseInt('1000'.substr(0, subtraction_row_array[0])))), Math.floor(Math.random() * (9 * '1000'.substr(0, subtraction_row_array[1])) + (parseInt('1000'.substr(0, subtraction_row_array[1]))))];

	var numbers = [get_number(subtraction_row_array[0], 0), get_number(subtraction_row_array[1], 1)];

	numbers.sort(numOrdD);

	for (var i = 0; i < subtraction_row_total; i ++)
		{
		var this_number = numbers[i];

		all_numbers.push(this_number);

		if (i == 0) correct_answer = this_number; else correct_answer -= this_number;

		if (i == subtraction_row_total - 1) game_contents += '-<span style="background-image:url(images/underline.png);">';

		game_contents += pad(this_number, 4, i) + '<br>';
		}

	game_contents += '</span>';
	}

if (game_type == 'division')
	{
	game_contents = '<div style="margin-left:-44px;text-align:right;width:317px;">';

	//var numbers = [Math.floor(Math.random() * (9 * '1000'.substr(0, division_row_array[0])) + (parseInt('1000'.substr(0, division_row_array[0])))), Math.floor(Math.random() * (9 * '1000'.substr(0, division_row_array[1])) + (parseInt('1000'.substr(0, division_row_array[1]))))];

	var numbers = [get_number(division_row_array[0], 0), get_number(division_row_array[1], 1)];

	numbers.sort(numOrdA);

	correct_answer = numbers[1] / numbers[0];

	if (!use_remainder)
		{
		correct_answer = parseInt(correct_answer);
		numbers[1] = numbers[0] * correct_answer;
		}
		else
		{
		correct_answer = (parseInt(correct_answer)) + 'r' + (numbers[1] - (parseInt(correct_answer) * numbers[0]));
		$('.remainder_input').show();
		}

	for (var i = 0; i < division_row_total; i ++)
		{
		var this_number = numbers[i];

		all_numbers.push(this_number);

		if (i == division_row_total - 1) game_contents += '<span style="border-top:2px solid #000;border-left:2px solid #000;padding:0px;margin:0px;">';

		game_contents += pad(this_number, 4, i);
		}

	game_contents += '</span>';
	}

all_numbers.push(correct_answer);

game_contents += (game_type != 'division' ? pad(correct_answer, 4, i) : '<span id="row_' + i + '" style="position:absolute;top:50px;right:86px;letter-spacing:6px;">' + correct_answer + '</span>') + '</div>';

document.getElementById('game_inner').innerHTML = game_contents;

if (document.getElementById('vary_checkbox').checked)
	{
	var correct_answer_row = Math.floor(Math.random() * all_numbers.length);
	correct_answer = all_numbers[correct_answer_row];
	document.getElementById('row_' + correct_answer_row).style.visibility = 'hidden';	//innerHTML = '?';
	}
	else
	{
	var correct_answer_row = i;
	document.getElementById('row_' + correct_answer_row).style.visibility = 'hidden';
	}

//questions_array[question_number - 1] = game_type + '|' + correct_answer_row + '|' + all_numbers.join('|');

all_numbers[correct_answer_row] = '?';

questions_array[question_number - 1] = '';

for (var i = 0; i < all_numbers.length; i ++)
	{
	questions_array[question_number - 1] += all_numbers[i];
	if (i < all_numbers.length - 2) questions_array[question_number - 1] += operator_symbol[game_type]; else if (i == all_numbers.length - 2) questions_array[question_number - 1] += '=';
	}

console.log(questions_array[question_number - 1]);
}

function show_next_question_teachers()
{
$('.remainder_input').hide();

if (question_number > max_questions) return;

question_number ++;

reset();

max_questions = custom_questions.length;

document.getElementById('result_overlay_div').style.display = 'none';
document.getElementById('problem_div').innerHTML = question_number + '/' + max_questions;
document.getElementById('score_div').innerHTML = parseInt((100 / max_questions) * Math.floor(score)) + '%';
document.getElementById('result_div').value = '';
document.getElementById('result_int_div').value = '';
document.getElementById('result_rem_div').value = '';

var game_contents = '';

correct_answer = 0;
all_numbers = [];

already_guessed = false;

var question_data = custom_questions[question_number - 1].split('~');

var this_question = question_data[0];

document.getElementById('vary_checkbox').checked = question_data.length > 1 && question_data[1] == 1 ? true : false;

if (question_data.length == 3) use_remainder = question_data[2] == 1;

//console.log(question_data.length + ' ' + use_remainder);

if (this_question.indexOf('+') > -1)
	{
	teachers_game_type = 'addition';

	game_contents = '<div style="margin-left:35px;text-align:right;width:200px;">';

	var question_data = this_question.split('+');

	addition_row_total = question_data.length;

	for (var i = 0; i < addition_row_total; i ++)
		{
		if (question_data[i] == Math.floor(question_data[i]))
			{
			var this_number = Math.floor(question_data[i]);

			correct_answer += this_number;

			all_numbers.push(this_number);

			if (i == addition_row_total - 1) game_contents += '+<span style="background-image:url(images/underline.png);">';

			game_contents += pad(this_number, 4, i) + '<br>';
			}
		}

	game_contents += '</span>';
	}

if (this_question.indexOf('x') > -1)
	{
	teachers_game_type = 'multiplication';

	game_contents = '<div style="margin-left:35px;text-align:right;width:200px;">';

	var question_data = this_question.split('x');

	multiplication_row_total = question_data.length;

	for (var i = 0; i < multiplication_row_total; i ++)
		{
		if (question_data[i] == Math.floor(question_data[i]))
			{
			var this_number = Math.floor(question_data[i]);

			if (i == 0) correct_answer = this_number; else correct_answer *= this_number;

			if (i == multiplication_row_total - 1) game_contents += 'x<span style="background-image:url(images/underline.png);">';

			game_contents += pad(this_number, 4, i) + '<br>';

			all_numbers.push(this_number);
			}
		}

	game_contents += '</span>';
	}

if (this_question.indexOf('-') > -1)
	{
	teachers_game_type = 'subtraction';

	game_contents = '<div style="margin-left:35px;text-align:right;width:200px;">';

	var question_data = this_question.split('-');

	subtraction_row_total = question_data.length;

	var numbers = [question_data[0], question_data[1]];

	numbers.sort(numOrdD);

	for (var i = 0; i < subtraction_row_total; i ++)
		{
		var this_number = numbers[i];

		if (i == 0) correct_answer = this_number; else correct_answer -= this_number;

		if (i == subtraction_row_total - 1) game_contents += '-<span style="background-image:url(images/underline.png);">';

		game_contents += pad(this_number, 4, i) + '<br>';

		all_numbers.push(this_number);
		}

	game_contents += '</span>';
	}

if (this_question.indexOf('/') > -1)
	{
	teachers_game_type = 'division';

	game_contents = '<div style="margin-left:-44px;text-align:right;width:317px;">';

	var question_data = this_question.split('/');

	division_row_total = question_data.length;

	var numbers = [question_data[0], question_data[1]];

	numbers.sort(numOrdA);

	correct_answer = numbers[1] / numbers[0];

	correct_answer = (parseInt(correct_answer)) + 'r' + (numbers[1] - (parseInt(correct_answer) * numbers[0]));
	$('.remainder_input').show();

	for (var i = 0; i < division_row_total; i ++)
		{
		var this_number = numbers[i];

		if (i == division_row_total - 1) game_contents += '<span style="border-top:2px solid #000;border-left:2px solid #000;padding:0px;margin:0px;">';

		game_contents += pad(this_number, 4, i);

		all_numbers.push(this_number);
		}

	game_contents += '</span>';
	}

all_numbers.push(correct_answer);

game_contents += (teachers_game_type != 'division' ? pad(correct_answer, 4, i) : '<span id="row_' + i + '" style="position:absolute;top:50px;right:86px;letter-spacing:6px;">' + correct_answer + '</span>') + '</div>';

document.getElementById('game_inner').innerHTML = game_contents;

if (document.getElementById('vary_checkbox').checked)
	{
	var correct_answer_row = Math.floor(Math.random() * all_numbers.length);
	correct_answer = all_numbers[correct_answer_row];
	document.getElementById('row_' + correct_answer_row).style.visibility = 'hidden';	//innerHTML = '?';
	}
	else
	{
	var correct_answer_row = i;
	document.getElementById('row_' + correct_answer_row).style.visibility = 'hidden';
	}

//questions_array[question_number - 1] = teachers_game_type + '|' + correct_answer_row + '|' + all_numbers.join('|');

all_numbers[correct_answer_row] = '?';

questions_array[question_number - 1] = '';

for (var i = 0; i < all_numbers.length; i ++)
	{
	questions_array[question_number - 1] += all_numbers[i];
	if (i < all_numbers.length - 2) questions_array[question_number - 1] += operator_symbol[teachers_game_type]; else if (i == all_numbers.length - 2) questions_array[question_number - 1] += '=';
	}

//console.log(questions_array[question_number - 1]);
}

function preload_problems()
{
if (!preload_questions) return;

custom_questions = preload_questions.split('|');
var custom_question_list = '<form id="problem_form"><table>';

for (var i = 0; i < custom_questions.length; i ++)
	{
	var question_data = custom_questions[i].split('~');
	custom_question_list += '<tr><td style="width:20px;"><input type="checkbox" id="checkbox_' + i + '"></td><td style="width:170px;">' + question_data[0] + '</td><td>' + (question_data.length > 0 && question_data[1] == '1' ? ' vary equations' : '') + '</td></tr>';
	}

custom_question_number = i;

document.getElementById('problem_list_div').innerHTML = custom_question_list + '</table></form>';
}

function add_problem()
{
if (document.getElementById('problem_input').value == '') return false;

var this_problem = document.getElementById('problem_input').value;

this_problem = this_problem.replace(/\x2a/g, 'x');
this_problem = this_problem.replace(/X/g, 'x');
this_problem = this_problem.replace(/|/g, '');
this_problem = this_problem.replace(/~/g, '');

custom_questions[custom_question_number] = this_problem + '~' + (document.getElementById('problem_input_vary_checkbox').checked ? 1 : 0);
custom_question_number ++;

var custom_question_list = '<form id="problem_form"><table>';

for (var i = 0; i < custom_question_number; i ++)
	{
	//custom_question_list += '<tr><td><input type="checkbox" id="checkbox_' + i + '"></td><td>' + custom_questions[i] + '</td></tr>';
	var question_data = custom_questions[i].split('~');

	custom_question_list += '<tr><td style="width:20px;"><input type="checkbox" id="checkbox_' + i + '"></td><td style="width:170px;">' + question_data[0] + '</td><td style="font-weight:normal;font-size:12px;">' + (question_data.length > 0 && question_data[1] == '1' ? ' vary&nbsp;equations' : '') + '</td></tr>';
	}

document.getElementById('problem_list_div').innerHTML = custom_question_list + '</table></form>';
document.getElementById('problem_input').value = '';
document.getElementById('problem_input_vary_checkbox').checked = false;
}

function delete_problem()
{
if (custom_question_number < 1) return false;

var custom_questions_new = [];

var question_count = 0;

for (var i = 0; i < document.getElementById('problem_form').length; i ++)
	{
	if (!document.getElementById('problem_form')[i].checked) custom_questions_new[question_count ++] = custom_questions[i];
	}

custom_questions = [];
custom_questions = custom_questions_new;

custom_question_number = custom_questions.length;

var custom_question_list = '<form id="problem_form"><table>';

var custom_question_list = '<form id="problem_form"><table>';

for (var i = 0; i < custom_question_number; i ++)
	{
	var question_data = custom_questions[i].split('~');

	custom_question_list += '<tr><td style="width:20px;"><input type="checkbox" id="checkbox_' + i + '"></td><td style="width:170px;">' + question_data[0] + '</td><td style="font-weight:normal;font-size:12px;">' + (question_data.length > 0 && question_data[1] == '1' ? ' vary&nbsp;equations' : '') + '</td></tr>';
	}


document.getElementById('problem_list_div').innerHTML = custom_question_list + '</table></form>';
}

function custom_finished()
{
if (custom_question_number == 0)
	{
	document.getElementById('menu_div').style.display = 'block';
	document.getElementById('options_div_teachers').style.display='none';
	}
	else
	{
	var custom_questions_psv = custom_questions.join('|');
	$('#options_div_teachers').hide();
	game_type = 'teachers';
	start_game();
	}
}

function do_line(x1, y1, x2, y2, id)
{
if (id > -1 && document.getElementById('sprite_' + id) != null)
	{
	var line = document.getElementById('sprite_' + id);
	}
	else
	{
	//alert(document.getElementById('sprite_' + id));
	var line = document.createElement('line');
	line.id = 'sprite_' + sprite_number;
	sprite_number ++;
	}

if (x2 < x1)
	{
	var temp = x1;
	x1 = x2;
	x2 = temp;
	temp = y1;
	y1 = y2;
	y2 = temp;
	}

var length = Math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
line.style.width = length + "px";

if (IE)
	{
	line.style.top = (y2 > y1) ? y1 + "px" : y2 + "px";
	line.style.left = x1 + "px";
	var nCos = (x2-x1)/length;
	var nSin = (y2-y1)/length;
	line.style.filter = "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=" + nCos + ", M12=" + -1*nSin + ", M21=" + nSin + ", M22=" + nCos + ")";
	}
	else
	{
	var angle = Math.atan((y2-y1)/(x2-x1));
	line.style.top = y1 + 0.5*length*Math.sin(angle) + "px";
	line.style.left = x1 - 0.5*length*(1 - Math.cos(angle)) + "px";
	line.style.MozTransform = line.style.WebkitTransform = line.style.OTransform= "rotate(" + angle + "rad)";
	}

if (id < 0)
	{
	document.getElementById('main_div').appendChild(line);
	line.onmouseup = stop_line;
	}

return line;
}

function numOrdA(a, b){ return (a-b); }
function numOrdD(a, b){ return (b-a); }

function pad(number, length, row)
{
number = Math.floor(number);

var padding_required = length - (number + "").length;

var monospace = '';
var number_string = number.toString();

for (var i in number_string)
	{
	monospace += '<span class="mono_text">' + number_string[i] + '</span>';
	}

for (var i = 0; i < padding_required; i ++)
	{
	monospace = '<span class="mono_text" style="visibility:hidden;">0</span>' + monospace;
	}

for (var i = 0; i < padding_required; i ++)
	{
	number = '<span style="visibility:hidden;">0</span>' + number;
	}

return '<span id="row_' + row + '">' + monospace + '</span>';
}

function validate_integer(e, element)
{
var keynum;
var keychar;
var numcheck;

if(window.event) keynum = e.keyCode; else if(e.which) keynum = e.which;

keychar = String.fromCharCode(keynum);

if (keynum == 82 && (game_type == 'division' || teachers_game_type == 'division') && element.value.length > 0 && element.value.indexOf('r') == -1 && !e.shiftKey) return;

 if ( keynum == 46 || keynum == 8 || keynum == 9 || keynum == 27 || keynum == 13 || (keynum == 65 && e.ctrlKey === true) || (keynum >= 35 && keynum <= 39))
 	{
	return;
	}
	else
	{
	if (e.shiftKey || (keynum < 48 || keynum > 57) && (keynum < 96 || keynum > 105 ))
		{
		//event.preventDefault();
		return false;
		}
	}
}

function toggle_music()
{
audio_on = !audio_on;

if (!audio_on) stop_sound(2); else play_sound(2);
}

function check_answer()
{
if ($('.remainder_input').css('display') == 'block')
	{
	if (document.getElementById('result_int_div').value == '' || document.getElementById('result_overlay_div').style.display == 'block') return false;
	var entered_answer = document.getElementById('result_int_div').value + 'r' + document.getElementById('result_rem_div').value;
	}
	else
	{
	if (document.getElementById('result_div').value == '' || document.getElementById('result_overlay_div').style.display == 'block') return false;
	var entered_answer = document.getElementById('result_div').value;
	}

if ((correct_answer + "").indexOf('r') > -1 && (entered_answer + "").indexOf('r') == -1) entered_answer += 'r0';

if (entered_answer == $.trim(correct_answer))
	{
	play_sound(0);
	document.getElementById('result_overlay_div').innerHTML = '<img src="images/popup_correct.png"><br><div class="button" style="top:218px;left:17px;width:147px;height:59px" onclick="document.getElementById(\'result_overlay_div\').style.display = \'none\';"></div><div class="button" style="top:218px;left:219px;width:147px;height:59px" onclick="show_next_question();"></div>';

	if (!already_guessed)
		{
		answers_array[question_number - 1] = 'Correct';
		score ++;
		}
	}
	else
	{
	answers_array[question_number - 1] = 'Incorrect';
	already_guessed = true;
	play_sound(1);
	document.getElementById('result_overlay_div').innerHTML = '<img src="images/popup_wrong.png"><br><div class="button" style="top:218px;left:17px;width:147px;height:59px" onclick="document.getElementById(\'result_overlay_div\').style.display = \'none\';"></div><div class="button" style="top:218px;left:219px;width:147px;height:59px" onclick="show_next_question();"></div>';
	}

if (question_number >= max_questions)
	{
	document.getElementById('result_overlay_div').innerHTML += '<img src="images/popup_scores_button.png" class="button" style="top:214px;left:6px;" onclick="game_over();">';
	}

document.getElementById('result_overlay_div').style.display = 'block';
}

function game_over()
{
reset();

document.getElementById('game_div').style.display = 'none';
document.getElementById('game_over_div').style.display = 'block';

var score_percent = ((100 / max_questions) * score);
var cert_text = '';
var medal = false;

if (score_percent == 0)
	{
	cert_text = 'Try your best next time.';
	}

if (score_percent > 0 && score_percent < 50) medal = 'Bronze';
if (score_percent >= 50) medal = 'Silver';
if (score_percent == 100) medal = 'Gold';

if (medal)
	{
	cert_text = '<div style="width:285px;text-align:center;">You are awarded with a ' + medal + ' Medal for having scored ' + score + ' points.</div><img src="images/' + medal + '.png" style="position:absolute;top:19px;left:300px;">';
	}

document.getElementById('game_over_text').innerHTML = cert_text;

var questions_psv = questions_array.join('|');
var answers_psv = answers_array.join('|');

clearInterval(time_taken_interval);
}

function update_score_complete(data)
{
parent.update_score_header(data);
}

function change_problems(new_number, highlight_element)
{
document.getElementById('problems_' + max_questions).src = 'images/' + max_questions + '_unselected.png';
max_questions = new_number;
document.getElementById('problems_' + max_questions).src = 'images/' + max_questions + '_selected.png';
//document.getElementById('problem_number_highlight').style.left = highlight_element.offsetLeft + 'px';
}

function addition_rows(number_of_rows)
{
for (var i = 1; i < 5; i ++)
	{
	if (i <= number_of_rows) document.getElementById('addition_row_' + i).style.display = 'table-row'; else document.getElementById('addition_row_' + i).style.display = 'none';
	if (i == number_of_rows) document.getElementById('addition_sign_' + i).innerHTML = '+'; else document.getElementById('addition_sign_' + i).innerHTML = '&nbsp;';
	}

addition_row_total = number_of_rows;
}

function show_checkboxes(number_of_digits, row_number)
{
var mults_row = document.getElementById(game_type + '_mults_' + row_number);

if (number_of_digits == 2)
	{
	mults_row.style.display = 'table-cell';
	mults_row.innerHTML = mults_row.innerHTML.replace(/ 100 /g, ' 10 ');
	}
	else if (number_of_digits == 3)
	{
	mults_row.style.display = 'table-cell';
	mults_row.innerHTML = mults_row.innerHTML.replace(/ 10 /g, ' 100 ');
	}
	else
	{
	mults_row.style.display = 'none';
	}

if (game_type == 'division')
	{
	if (document.getElementById('division_mults_1').style.display == 'none' && document.getElementById('division_mults_2').style.display != 'none')
		{
		document.getElementById('division_mults_1').style.visibility = 'hidden';
		document.getElementById('division_mults_1').style.display = 'table-cell';
		}
		else
		{
		document.getElementById('division_mults_1').style.visibility = 'visible';
		}
	}
}

function addition_row_digits(row_number, number_of_digits)
{
document.getElementById('addition_row_digits_' + row_number).innerHTML = all_digits.substr(0, number_of_digits);
addition_row_array[row_number - 1] = number_of_digits;
show_checkboxes(number_of_digits, row_number);
}

function multiplication_row_digits(row_number, number_of_digits)
{
multiplication_row_array[row_number - 1] = number_of_digits;

if (multiplication_row_array[1] > multiplication_row_array[0]) multiplication_row_array[1] = multiplication_row_array[0];

document.getElementById('multiplication_row_digits_1').innerHTML = all_digits.substr(0, multiplication_row_array[0]);
document.getElementById('multiplication_row_digits_2').innerHTML = all_digits.substr(0, multiplication_row_array[1]);

show_checkboxes(number_of_digits, row_number);
}

function subtraction_row_digits(row_number, number_of_digits)
{
subtraction_row_array[row_number - 1] = number_of_digits;

if (subtraction_row_array[1] > subtraction_row_array[0]) subtraction_row_array[1] = subtraction_row_array[0];

document.getElementById('subtraction_row_digits_1').innerHTML = all_digits.substr(0, subtraction_row_array[0]);
document.getElementById('subtraction_row_digits_2').innerHTML = all_digits.substr(0, subtraction_row_array[1]);

show_checkboxes(number_of_digits, row_number);
}

function division_row_digits(row_number, number_of_digits)
{
division_row_array[row_number - 1] = number_of_digits;

if (division_row_array[0] > division_row_array[1]) division_row_array[1] = division_row_array[0];

document.getElementById('division_row_digits_1').innerHTML = all_digits.substr(0, division_row_array[0]);
document.getElementById('division_row_digits_2').innerHTML = all_digits.substr(0, division_row_array[1]);

show_checkboxes(number_of_digits, row_number);
}

function paper_type(selected_type)
{
document.getElementById('game_div').style.background = 'url(images/game_background_' + selected_type + '.png)';
}

function number_clicked(number, element, e)
{
if (number.toString().indexOf('_small') == -1)
	{
	var new_sprite = add_sprite('sprite_' + sprite_number, parseInt(element.style.left), parseInt(element.style.top), 28, 34, 'images/' + number + '.png', 'img');
	}
	else
	{
	var new_sprite = add_sprite('sprite_' + sprite_number, parseInt(element.style.left), parseInt(element.style.top), 14, 17, 'images/' + number.replace('_small', '') + '.png', 'img');
	}

start_moving_sprite(e, new_sprite);
new_sprite.sprite_number = sprite_number;
new_sprite.style.cursor = 'pointer';
new_sprite.onmousedown = start_moving_sprite;
new_sprite.ontouchstart = start_moving_sprite;
sprite_number ++;
}

function undo()
{
if (sprite_number == 0) return false;
sprite_number --;
remove_sprite('sprite_' + sprite_number);
}

function reset()
{
for (var i = 0; i < sprite_number; i ++)
	{
	remove_sprite('sprite_' + i);
	}

sprite_number = 0;
}

function display_time()
{
var seconds = time_left % 60;
var minutes = (time_left - seconds) / 60;
if (minutes <= 0) minutes = '00'; else if (minutes < 10) minutes = '0' + minutes;
if (seconds <= 0) seconds = '00'; else if (seconds < 10) seconds = '0' + seconds;

document.getElementById('timer_div').innerHTML = minutes + ':' + seconds;
}

function text_time(this_time)
{
var seconds = this_time % 60;
var minutes = (this_time - seconds) / 60;
if (minutes <= 0) minutes = ''; else if (minutes == 1) minutes = minutes + ' minute'; else minutes = minutes + ' minutes';
if (seconds <= 0) seconds = ''; else if (seconds == 1) seconds = seconds + ' second'; else seconds = seconds + ' seconds';
if (minutes != '' && seconds != '') minutes += ' and ';
return minutes + seconds;
}

function play_sound(sound_number)
{
if (audio_on)
	{
	if (!sounds_loaded[sound_number])
		{
		sounds[sound_number].load();
		sounds_loaded[sound_number] = true;
		}

	sounds[sound_number].play();
	}
}

function stop_sound(sound_number)
{
try
	{
	sounds[sound_number].pause();
	sounds[sound_number].currentTime = 0;
	}
catch(e)
	{
	}
}

function mute(sid)
{
sid.pause();
}

function _pl()
{
this.Audio.src = this.wav;
}

function _st()
{
this.Audio.src = '';
}

function _cu(x)
{
}

function nf()
{
return;
}

function audio(wav)
{
if(document.all)
	{
	this.Audio = document.createElement('bgsound');

	if(this.Audio)
		{
		this.wav = wav;
		this.Audio.loop = 0;
		this.Audio.autostart = false;
		//this.Audio.src = wav;
		document.getElementById('sb').appendChild(this.Audio);
		this.play = _pl;
		this.pause = _st;
		this.stop = _st;
		this.currentTime = _cu;
		return this;
		}
	}

this.play = nf;
this.stop = nf;

return this;
}

function load_audio()
{
try
	{
	sounds[0] = new Audio("");
	sound_type = 'html5';
	}

catch(err)
	{
	sound_type = 'ie';
	}

if (!!(sounds[0].canPlayType && sounds[0].canPlayType('audio/mpeg;').replace(/no/, ''))) sound_extension = 'mp3'; else sound_extension = 'ogg';

for (var i=0; i<sound_files.length; i++)
	{
	if (sound_type == 'html5')
		{
		sounds[i] = new Audio("");
		sounds[i].src = 'sounds/' + sound_files[i] + '.' + sound_extension;
		}
		else
		{
		sounds[i] = new audio('sounds/' + sound_files[i] + '.mp3');
		}

	if (IE) sounds_loaded[i] = true;
	}
}

function leftClick(e)
{
window.focus();
if (!e) e = event;
return ((typeof e.which == 'undefined') ? (e.button == 1) : (e.which == 1 || e.button == 0));
}

function nrc(e)
{
if (leftClick(e) == false)
	{
	return ce(e);
	}
}

function cp(e)
{
if (!e) e = event;
if (e.stopPropagation) e.stopPropagation(); else if (typeof e.cancelBubble != 'undefined') e.cancelBubble = true;
}

function ce(e)
{
if (!e) e = window.event;

if (typeof e.preventDefault != 'undefined')
	{
	e.preventDefault();
	}
	else if (typeof e.cancelBubble != 'undefined')
	{
	e.returnValue = 0;
	e.cancelBubble = true;
	}

return false;
}

function fade(element_to_fade, start_opacity, fade_speed)
{
var element_id = document.getElementById(element_to_fade);

if(element_to_fade == null) return;

element_id.style.opacity = start_opacity != null ? start_opacity : 0.05;
element_id.fade_direction = fade_speed != null ? fade_speed : 0.05;
setTimeout("fade_continue('" + element_to_fade + "')", 30);
}

function fade_continue(element_to_fade)
{
var element_id = document.getElementById(element_to_fade);
var new_opacity = (element_id.style.opacity * 1) + element_id.fade_direction;
new_opacity = new_opacity.toFixed(2);

if (new_opacity >= 0 && new_opacity <= 1)
	{
	element_id.style.opacity = new_opacity;
	element_id.style.filter = 'alpha(opacity = ' + (new_opacity * 100) + ')';

	if (new_opacity > 0 && new_opacity < 1) setTimeout("fade_continue('" + element_to_fade + "')", 30);
	}
}

function scale_div(obj, x, y)
{
if (transform_property)
	{
	obj.style[transform_property] = "scale(" + x + ", " + y + ")";
	}
	else
	{
	obj.style.filter = 'progid:DXImageTransform.Microsoft.Matrix(sizingMethod="auto expand", M11 = ' + x + ', M12 = ' + 0 + ', M21 = ' + 0 + ', M22 = ' + y + ')';
	//obj.style.marginLeft = '0px';	//(parseInt(obj.style.width) - (parseInt(obj.style.width) * x)) / 2 + 'px';
	//obj.style.marginTop = '0px';	//(parseInt(obj.style.height) - (parseInt(obj.style.height) * y)) / 2 + 'px';
	}
}

function get_transform_property(element)							//find out which CSS tags this browser uses for scaling and other graphical transforms
{
var properties = ['transform', 'WebkitTransform', 'MozTransform','OTransform'];

while (this_property = properties.shift())
	{
        if (typeof element.style[this_property] != 'undefined') return this_property;
	}

return false;
}

function get_viewport_width()
{
var viewportWidth = 0;

if (typeof(window.innerWidth) == 'number')
	{
	viewportWidth = window.innerWidth;
	}
	else if (document.documentElement && document.documentElement.clientWidth)
	{
	viewportWidth = document.documentElement.clientWidth;
	}
	else if (document.body && document.body.clientWidth)
	{
	viewportWidth = document.body.clientWidth;
	}
	else if (screen.width)
	{
	viewportWidth = screen.width;
	}

return viewportWidth;
}

function get_viewport_height()
{
if (typeof window.innerWidth != 'undefined')
	{
	var viewport_width = window.innerWidth;
	var viewport_height = window.innerHeight;
	}
	else if (typeof document.documentElement != 'undefined' && typeof document.documentElement.clientWidth != 'undefined' && document.documentElement.clientWidth != 0)
	{
	var viewport_width = document.documentElement.clientWidth;
	var viewport_height = document.documentElement.clientHeight;
	}
	else
	{
	var viewport_width = document.getElementsByTagName('body')[0].clientWidth;
	var viewport_height = document.getElementsByTagName('body')[0].clientHeight;
	}

return viewport_height;
}

function m(e)
{
if (!e) var e = window.event;

if (e.pageX != null) mousex = e.pageX;
else if (e.clientX) mousex = e.clientX + (document.documentElement.scrollLeft ? document.documentElement.scrollLeft : document.body.scrollLeft);
else mousex = 0;

if (e.pageY != null) mousey = e.pageY;
else if (e.clientY) mousey = e.clientY + (document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop);
else mousey = 0;

if (e.touches)
	{
	mousex = e.touches[0].pageX;
	mousey = e.touches[0].pageY;
	}

mousex /= zoom;
mousey /= zoom;

if (moving_sprite_number != -1)
	{
	moving_sprite_element_id.style.left = mousex - moving_sprite_element_offset_x + 'px';
	moving_sprite_element_id.style.top = mousey - moving_sprite_element_offset_y + 'px';
	ce(e);
	}

if (line_start_x)
	{
	line_end_x = mousex;
	line_end_y = mousey;

	do_line(line_start_x, line_start_y, line_end_x, line_end_y, line_number);
	}
}

function start_moving_sprite(e, sprite_element_id)
{
if (!e) var e = window.event;

ce(e);

if (e.touches)
	{
	mousex = e.touches[0].pageX;
	mousey = e.touches[0].pageY;

	mousex /= zoom;
	mousey /= zoom;
	}

if (sprite_element_id === undefined) sprite_element_id = (e.target) ? e.target : e.srcElement;

moving_sprite_number = sprite_element_id.sprite_number;
moving_sprite_element_id = sprite_element_id;
moving_sprite_element_offset_x = mousex - parseInt(sprite_element_id.style.left);
moving_sprite_element_offset_y = mousey - parseInt(sprite_element_id.style.top);
moving_sprite_element_start_x = parseInt(sprite_element_id.style.left);
moving_sprite_element_start_y = parseInt(sprite_element_id.style.top);
}

function stop_moving_sprite()
{
if (line_start_x) return stop_line();

if (!moving_sprite_element_id) return;	// false;

moving_sprite_number = -1;
moving_sprite_element_id = -1;
moving_sprite_element_offset_x = 0;
moving_sprite_element_offset_y = 0;
moving_sprite_element_start_x = 0;
moving_sprite_element_start_y = 0;
}

function start_line(e)
{
if (!e) var e = window.event;

ce(e);

if (e.touches)
	{
	mousex = e.touches[0].pageX;
	mousey = e.touches[0].pageY;

	mousex /= zoom;
	mousey /= zoom;
	}

line_number = sprite_number;

do_line(mousex, mousey, mousex + 1, mousey + 1, -1);

line_start_x = mousex;
line_start_y = mousey;

line_end_x = mousex;
line_end_y = mousey;
}

function stop_line()
{
if (!line_start_x) return false;

if (line_start_x == line_end_x && line_start_y == line_end_y)
	{
	remove_sprite('sprite_' + line_number);
	sprite_number --;
	}

line_start_x = false;
}

function add_sprite(id, x, y, width, height, image, classname)
{
if (document.getElementById(id) != null) return false;

var new_element = document.createElement(classname);
var new_element_style = new_element.style;
new_element.id = id;
new_element_style.left = x + 'px';
new_element_style.top = y + 'px';
new_element_style.width = width + 'px';
new_element_style.height = height + 'px';

if (image)
	{
	if (classname != 'img')
		{
		new_element_style.backgroundImage = 'url(' + image + ')';
		}
		else
		{
		new_element.style.position = 'absolute';
		new_element.src = image;
		}
	}

document.getElementById('main_div').appendChild(new_element);

return new_element;
}

function remove_sprite(id)
{
var element_id = document.getElementById(id);
if (element_id && element_id != null) document.getElementById('main_div').removeChild(element_id);
}