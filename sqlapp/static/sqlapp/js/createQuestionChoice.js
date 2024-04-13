
 function twoOfFour() {
    let answer = document.getElementById("id_answer");

    /*let messageElement = document.getElementById("id_answer");*/
    // answerの値が存在しない、または空の場合、関数を終了
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    wronganswer4 = document.getElementById("id_wronganswer4");
    wronganswer5 = document.getElementById("id_wronganswer5");
    wronganswer6 = document.getElementById("id_wronganswer6");
   
    let abText = "A, B";
    let acText = "A, C";
    let adText = "A, D";
    let bcText = "B, C";
    let bdText = "B, D";
    let cdText = "C, D";  

    document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "A,B"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = bcText;
        wronganswer5.innerText = bdText;
        answer.value = "A, B";
    }else if(answerValue == "B,C"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "B, C";
    }else if(answerValue == "A,C"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "A, C";
    }else if(answerValue == "A,D"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = acText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "A, D";
    }else if(answerValue == "B,D"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = acText;
        answer.value = "B, D";
    }else if(answerValue == "C,D"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "C, D";
    }else{
        alert("「[半角大文字アルファベット][半角カンマ][半角大文字アルファベット]」の形式で入力してください。")
    }
  }

  function twoOfFourAiue() {
    answer = document.getElementById("id_answer");
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    wronganswer4 = document.getElementById("id_wronganswer4");
    wronganswer5 = document.getElementById("id_wronganswer5");
    wronganswer6 = document.getElementById("id_wronganswer6");
   
    abText = "ア、イ";
    acText = "ア、ウ";
    adText = "ア、エ";
    bcText = "イ、ウ";
    bdText = "イ、エ";
    cdText = "ウ、エ";  

    document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "ア、イ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = bcText;
        wronganswer5.innerText = bdText;
        answer.value = "ア、イ";
    }else if(answerValue == "イ、ウ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "イ、ウ";
    }else if(answerValue == "ア、ウ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "ア、ウ";
    }else if(answerValue == "ア、エ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = acText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "ア、エ";
    }else if(answerValue == "イ、エ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = acText;
        answer.value = "イ、エ";
    }else if(answerValue == "ウ、エ"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        answer.value = "ウ、エ";
    }else{
        alert("「[全角カタカナ][全角カンマ][全角カタカナ]」の形式で入力してください。")
    }
  }

  function twoOfFive() {
    answer = document.getElementById("id_answer");
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    wronganswer4 = document.getElementById("id_wronganswer4");
    wronganswer5 = document.getElementById("id_wronganswer5");
    wronganswer6 = document.getElementById("id_wronganswer6");
    wronganswer7 = document.getElementById("id_wronganswer7");
    wronganswer8 = document.getElementById("id_wronganswer8");
    wronganswer9 = document.getElementById("id_wronganswer9");
   
    abText = "A, B";
    acText = "A, C";
    adText = "A, D";
    bcText = "B, C";
    bdText = "B, D";
    cdText = "C, D";
    aeText = "A, E";
    beText = "B, E";
    ceText = "C, E";
    deText = "D, E";

    document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(18)').style.display = "block";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "A,B"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = bcText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "A, B";
    }else if(answerValue == "B,C"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "B, C";
    }else if(answerValue == "A,C"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "A, C";
    }else if(answerValue == "A,D"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = acText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "A, D";
    }else if(answerValue == "B,D"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = acText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "B, D";
    }else if(answerValue == "C,D"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "C, D";
    }else if(answerValue == "B,E"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = cdText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "B, E";
    }else if(answerValue == "C,E"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = cdText;
        wronganswer9.innerText = deText;
        answer.value = "C, E";
    }else if(answerValue == "D,E"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = cdText;
        answer.value = "D, E";
    }else if(answerValue == "A,E"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = cdText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "A, E";
    }else{
        alert("「[半角大文字アルファベット][半角カンマ][半角大文字アルファベット]」の形式で入力してください。")
    }
  }

  function twoOfFiveAiueo() {
    answer = document.getElementById("id_answer");
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    wronganswer4 = document.getElementById("id_wronganswer4");
    wronganswer5 = document.getElementById("id_wronganswer5");
    wronganswer6 = document.getElementById("id_wronganswer6");
    wronganswer7 = document.getElementById("id_wronganswer7");
    wronganswer8 = document.getElementById("id_wronganswer8");
    wronganswer9 = document.getElementById("id_wronganswer9");
   
    abText = "ア、イ";
    acText = "ア、ウ";
    adText = "ア、エ";
    bcText = "イ、ウ";
    bdText = "イ、エ";
    cdText = "ウ、エ";
    aeText = "ア、オ";
    beText = "イ、オ";
    ceText = "ウ、オ";
    deText = "エ、オ";

    document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(18)').style.display = "block";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "ア、イ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = bcText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "ア、イ";
    }else if(answerValue == "イ、ウ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = acText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "イ、ウ";
    }else if(answerValue == "ア、ウ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "ア、ウ";
    }else if(answerValue == "ア、エ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = acText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "ア、エ";
    }else if(answerValue == "イ、エ"){
        wronganswer1.innerText = cdText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = acText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "イ、エ";
    }else if(answerValue == "ウ、エ"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "ウ、エ";
    }else if(answerValue == "イ、オ"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = cdText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "イ、オ";
    }else if(answerValue == "ウ、オ"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = cdText;
        wronganswer9.innerText = deText;
        answer.value = "ウ、オ";
    }else if(answerValue == "エ、オ"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = aeText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = cdText;
        answer.value = "エ、オ";
    }else if(answerValue == "ア、オ"){
        wronganswer1.innerText = acText;
        wronganswer2.innerText = bcText;
        wronganswer3.innerText = adText;
        wronganswer4.innerText = abText;
        wronganswer5.innerText = bdText;
        wronganswer6.innerText = cdText;
        wronganswer7.innerText = beText;
        wronganswer8.innerText = ceText;
        wronganswer9.innerText = deText;
        answer.value = "ア、オ";
    }else{
        alert("「[全角カタカナ][全角カンマ][全角カタカナ]」の形式で入力してください。")
    }
  }

  function threeOfFive() {
    answer = document.getElementById("id_answer");
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    wronganswer4 = document.getElementById("id_wronganswer4");
    wronganswer5 = document.getElementById("id_wronganswer5");
    wronganswer6 = document.getElementById("id_wronganswer6");
    wronganswer7 = document.getElementById("id_wronganswer7");
    wronganswer8 = document.getElementById("id_wronganswer8");
    wronganswer9 = document.getElementById("id_wronganswer9");
   
    abcText = "A, B, C";
    abdText = "A, B, D";
    abeText = "A, B, E";
    acdText = "A, C, D";
    aceText = "A, C, E";
    adeText = "A, D, E";
    bcdText = "B, C, D";
    bceText = "B, C, E";
    bdeText = "B, D, E";
    cdeText = "C, D, E";

    document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(18)').style.display = "block";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "A,B,C"){
        wronganswer1.innerText = abdText;
        wronganswer2.innerText = abeText;
        wronganswer3.innerText = acdText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "A, B, C";
    }else if(answerValue == "A,B,D"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abeText;
        wronganswer3.innerText = acdText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "A, B, D";
    }else if(answerValue == "A,B,E"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = acdText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "A, B, E";
    }else if(answerValue == "A,C,D"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "A, C, D";
    }else if(answerValue == "A,C,E"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "A, C, E";
    }else if(answerValue == "B,C,D"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "B, C, D";
    }else if(answerValue == "B,C,E"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bcdText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "B, C, E";
    }else if(answerValue == "B,D,E"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bcdText;
        wronganswer8.innerText = bceText;
        wronganswer9.innerText = cdeText;
        answer.value = "B, D, E";
    }else if(answerValue == "C,D,E"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bcdText;
        wronganswer8.innerText = bceText;
        wronganswer9.innerText = bdeText;
        answer.value = "C, D, E";
    }else if(answerValue == "A,D,E"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "A, D, E";
    }else{
        alert("「[半角大文字アルファベット][半角カンマ][半角大文字アルファベット][半角カンマ][半角大文字アルファベット]」の形式で入力してください。")
    }
  }

  function threeOfFiveAiueo() {
    answer = document.getElementById("id_answer");
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    wronganswer4 = document.getElementById("id_wronganswer4");
    wronganswer5 = document.getElementById("id_wronganswer5");
    wronganswer6 = document.getElementById("id_wronganswer6");
    wronganswer7 = document.getElementById("id_wronganswer7");
    wronganswer8 = document.getElementById("id_wronganswer8");
    wronganswer9 = document.getElementById("id_wronganswer9");
   
    abcText = "ア、イ、ウ";
    abdText = "ア、イ、エ";
    abeText = "ア、イ、オ";
    acdText = "ア、ウ、エ";
    aceText = "ア、ウ、オ";
    adeText = "ア、エ、オ";
    bcdText = "イ、ウ、エ";
    bceText = "イ、ウ、オ";
    bdeText = "イ、エ、オ";
    cdeText = "ウ、エ、オ";

    document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
    document.querySelector('.yokonarabi p:nth-child(18)').style.display = "block";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "ア、イ、ウ"){
        wronganswer1.innerText = abdText;
        wronganswer2.innerText = abeText;
        wronganswer3.innerText = acdText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "ア、イ、ウ";
    }else if(answerValue == "ア、イ、エ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abeText;
        wronganswer3.innerText = acdText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "ア、イ、エ";
    }else if(answerValue == "ア、イ、オ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = acdText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "ア、イ、オ";
    }else if(answerValue == "ア、ウ、エ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = aceText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "ア、ウ、エ";
    }else if(answerValue == "ア、ウ、オ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = adeText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "ア、ウ、オ";
    }else if(answerValue == "イ、ウ、エ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "イ、ウ、エ";
    }else if(answerValue == "イ、ウ、オ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bcdText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "イ、ウ、オ";
    }else if(answerValue == "イ、エ、オ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bcdText;
        wronganswer8.innerText = bceText;
        wronganswer9.innerText = cdeText;
        answer.value = "イ、エ、オ";
    }else if(answerValue == "ウ、エ、オ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = adeText;
        wronganswer7.innerText = bcdText;
        wronganswer8.innerText = bceText;
        wronganswer9.innerText = bdeText;
        answer.value = "ウ、エ、オ";
    }else if(answerValue == "ア、エ、オ"){
        wronganswer1.innerText = abcText;
        wronganswer2.innerText = abdText;
        wronganswer3.innerText = abeText;
        wronganswer4.innerText = acdText;
        wronganswer5.innerText = aceText;
        wronganswer6.innerText = bcdText;
        wronganswer7.innerText = bceText;
        wronganswer8.innerText = bdeText;
        wronganswer9.innerText = cdeText;
        answer.value = "ア、エ、オ";
    }else{
        alert("「[全角カタカナ][全角カンマ][全角カタカナ][全角カンマ][全角カタカナ]」の形式で入力してください。")
    }
  }

  function aiue() {
    answer = document.getElementById("id_answer");
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    
    aText = "ア";
    iText = "イ";
    uText = "ウ";
    eText = "エ";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "ア"){
        wronganswer1.innerText = iText;
        wronganswer2.innerText = uText;
        wronganswer3.innerText = eText;
        answer.value = "ア";
        
    }else if(answerValue == "イ"){
        wronganswer1.innerText = aText;
        wronganswer2.innerText = uText;
        wronganswer3.innerText = eText;
        answer.value = "イ";
        
    }else if(answerValue == "ウ"){
        wronganswer1.innerText = aText;
        wronganswer2.innerText = iText;
        wronganswer3.innerText = eText;
        answer.value = "ウ";
        
    }else if(answerValue == "エ"){
        wronganswer1.innerText = aText;
        wronganswer2.innerText = iText;
        wronganswer3.innerText = uText;
        answer.value = "エ";
        
    }else{
        alert("「[全角カタカナ]」の形式で入力してください。")
    }
  }

  function abcd() {
    answer = document.getElementById("id_answer");
    if (!answer || !answer.value) {
        /*messageElement.innerText = "「正解」を入力してください";*/
        alert("まず「正解」を入力してください。")
        return;
    }
    wronganswer1 = document.getElementById("id_wronganswer1");
    wronganswer2 = document.getElementById("id_wronganswer2");
    wronganswer3 = document.getElementById("id_wronganswer3");
    
    aText = "A";
    bText = "B";
    cText = "C";
    dText = "D";

    let answerValue = answer.value.replace(/[\s\u3000]/g, '');

    if(answerValue == "A"){
        wronganswer1.innerText = bText;
        wronganswer2.innerText = cText;
        wronganswer3.innerText = dText;
        answer.value = "A";
        
    }else if(answerValue == "B"){
        wronganswer1.innerText = aText;
        wronganswer2.innerText = cText;
        wronganswer3.innerText = dText;
        answer.value = "B";
        
    }else if(answerValue == "C"){
        wronganswer1.innerText = aText;
        wronganswer2.innerText = bText;
        wronganswer3.innerText = dText;
        answer.value = "C";
        
    }else if(answerValue == "D"){
        wronganswer1.innerText = aText;
        wronganswer2.innerText = bText;
        wronganswer3.innerText = cText;
        answer.value = "D";
        
    }else{
        alert("「[半角大文字アルファベット]」の形式で入力してください。")
    }
  }

function appearAuto() {
   
    categoryAuto = document.getElementById("id_category");
    shosekiAuto = document.getElementById("id_shoseki");
    
  
    if( shosekiAuto.innerText == 'Python3エンジニア認定基礎試験問題集' ) {
        categoryAutoText = 'Python3エンジニア認定基礎試験';
        categoryAuto.innerText = categoryAutoText;
        }
}

