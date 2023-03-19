var selected_subject_count = 0


function modify_subject_by_qual() {
    var qualification = document.getElementById("qualification").value;
    if (qualification === "IGCSE") {
        var hide_subs = document.getElementsByClassName("al_subject");
        var show_subs = document.getElementsByClassName("ig_subject");
        var special_subs = []
    } else {
        var hide_subs = document.getElementsByClassName("ig_subject");
        var show_subs = document.getElementsByClassName("al_subject");

        if (qualification === "AS-Level") {
            var special_subs = (document.getElementsByClassName("al_only"));
        } else {
            var special_subs = (document.getElementsByClassName("as_only"));
        }
    }
    for (let index = 0; index < show_subs.length; index++) {
        show_subs[index].style.display = "flex";
        show_subs[index].classList.remove("by_qual");
    }

    for (let index = 0; index < hide_subs.length; index++) {
        hide_subs[index].style.display = "none";
        hide_subs[index].classList.add("by_qual");
    }

    for (let index = 0; index < special_subs.length; index++) {
        special_subs[index].style.display = "none";
        special_subs[index].classList.add("by_qual");
    }
    document.getElementById("qualification_text").innerText = qualification;
}


for (let index = 0; index < document.getElementsByClassName("option").length; index++) {
    document.getElementsByClassName("option")[index].addEventListener("click", choose_option);
}


function choose_option(event) {
    var chosen_option = event.target;
    var parent_id = chosen_option.parentElement.parentElement.id;
    var inner_text = chosen_option.innerText
    var input_id = ""

    document.getElementById(chosen_option.id).classList.add("selected-option")

    // due to structure of html, for subject options the option text is one element lower, hence choosing from children
    if (parent_id === "subjects") {
        inner_text = chosen_option.children[0].innerText;
    }

    for (let index = 0; index < parent_id.length - 1; index++) {
        input_id = input_id + parent_id[index];
    }
    console.log(input_id)
    if (input_id !== "subject") {
        document.getElementById(input_id).value = chosen_option.id;
        document.getElementById(parent_id + "_choice").innerText = inner_text;
        if (input_id === 'qualification'){modify_subject_by_qual();}
        close_option(parent_id);
    }else{
        if (document.getElementById(parent_id).classList.value.includes('multiple')) {
            const new_input = document.createElement('input')
            new_input.name = 'subjects'
            new_input.type = 'text'
            new_input.setAttribute('hidden', '')
            new_input.value = chosen_option.id
            document.getElementById('edit_container').append(new_input)
            selected_subject_count++
            document.getElementById(parent_id + "_choice").innerText = selected_subject_count.toString() + " Subjects selected";
        }else {
            document.getElementById('subject').value = chosen_option.id
            close_option(parent_id);
            document.getElementById(parent_id + "_choice").innerText = inner_text;
        }
    // document.getElementById(parent_id + "_choice").innerText.classList.add("green");
    }
}


function display_options(options_id) {
    var options = document.getElementById(options_id);
    var container = document.getElementById("options_container");
    for (let index = 0; index < container.children.length; index++) {
        container.children[index].setAttribute("hidden", "")
    }
    container.style.display = "flex"
    options.style.display = "flex";

}


function close_option(options_id) {
    var options = document.getElementById(options_id);
    var container = document.getElementById("options_container");
    for (let index = 0; index < container.children.length; index++) {
        container.children[index].style.display = "none";
    }
    container.style.display = "none"
    options.style.display = "none";

}