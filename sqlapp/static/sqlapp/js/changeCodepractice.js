/*updateページの表示時に文字数に合わせてheightを変える*/
function adjustTextareaHeight(textarea) {
    textarea.style.height = ""; // まず高さをリセット
    textarea.style.height = textarea.scrollHeight + "px"; // スクロール高さに設定
}
document.addEventListener("DOMContentLoaded", function() {
 
    
    // ページ読み込み時にすべてのテキストエリアを調整
    document.querySelectorAll('textarea').forEach(function(textarea) {
        adjustTextareaHeight(textarea);
    });

    // 入力時にテキストエリアの高さを調整
    document.querySelectorAll('textarea').forEach(function(textarea) {
        textarea.addEventListener('input', function() {
            adjustTextareaHeight(textarea);
        });
    });
});



/*最初非表示のフォームを表示*/
let selectQuestion1 = document.querySelector('[name="question1"]');
selectQuestion1.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectQuestion1.value != ''){
        document.querySelector('.yokonarabi p:nth-child(6)').style.display = "block";
        
    };
}

let selectQuestion2 = document.querySelector('[name="question2"]');
selectQuestion2.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectQuestion2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(7)').style.display = "block";
        
    };
}


let selectReq1 = document.querySelector('[name="req1"]');
selectReq1.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectReq1.value != ''){
        document.querySelector('.yokonarabi p:nth-child(9)').style.display = "block";
    };
}
let selectReq2 = document.querySelector('[name="req2"]');
selectReq2.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectReq2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(10)').style.display = "block";
    };
}



let selectThumQ1 = document.querySelector('[name="thumbnailQ1"]');
selectThumQ1.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ1.value != ''){
        document.querySelector('.yokonarabi p:nth-child(12)').style.display = "block";
        
    };
}
let selectThumQ2= document.querySelector('[name="thumbnailQ2"]');
selectThumQ2.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
        
    };
}
let selectThumQ3 = document.querySelector('[name="thumbnailQ3"]');
selectThumQ3.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
        
    };
}
/*最初非表示のフォームを表示*/
let selectThumQ4 = document.querySelector('[name="thumbnailQ4"]');
selectThumQ4.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ4.value != ''){
        document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
        
    };
}

/*最初非表示のフォームを表示*/
let selectThumQ5 = document.querySelector('[name="thumbnailQ5"]');
selectThumQ5.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ5.value != ''){
        document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
        
    };
}
/*最初非表示のフォームを表示*/
let selectThumQ6 = document.querySelector('[name="thumbnailQ6"]');
selectThumQ6.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ6.value != ''){
        document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
        
    };
}
/*最初非表示のフォームを表示*/
let selectThumQ7 = document.querySelector('[name="thumbnailQ7"]');
selectThumQ7.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ7.value != ''){
        document.querySelector('.yokonarabi p:nth-child(18)').style.display = "block";
        
    };
}
/*最初非表示のフォームを表示*/
let selectThumQ8 = document.querySelector('[name="thumbnailQ8"]');
selectThumQ8.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ8.value != ''){
        document.querySelector('.yokonarabi p:nth-child(19)').style.display = "block";
        
    };
}
/*最初非表示のフォームを表示*/
let selectThumQ9 = document.querySelector('[name="thumbnailQ9"]');
selectThumQ9.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ9.value != ''){
        document.querySelector('.yokonarabi p:nth-child(20)').style.display = "block";
        
    };
}

let selectThumQ10 = document.querySelector('[name="thumbnailQ10"]');
selectThumQ10.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ10.value != ''){
        document.querySelector('.yokonarabi p:nth-child(21)').style.display = "block";
        
    };
}
let selectThumQ11 = document.querySelector('[name="thumbnailQ11"]');
selectThumQ11.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ11.value != ''){
        document.querySelector('.yokonarabi p:nth-child(22)').style.display = "block";
        
    };
}
let selectThumQ12 = document.querySelector('[name="thumbnailQ12"]');
selectThumQ12.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ12.value != ''){
        document.querySelector('.yokonarabi p:nth-child(23)').style.display = "block";
        
    };
}
let selectThumQ13 = document.querySelector('[name="thumbnailQ13"]');
selectThumQ13.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ13.value != ''){
        document.querySelector('.yokonarabi p:nth-child(24)').style.display = "block";
        
    };
}
let selectThumQ14 = document.querySelector('[name="thumbnailQ14"]');
selectThumQ14.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ14.value != ''){
        document.querySelector('.yokonarabi p:nth-child(25)').style.display = "block";
        
    };
}
let selectThumQ15 = document.querySelector('[name="thumbnailQ15"]');
selectThumQ15.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ15.value != ''){
        document.querySelector('.yokonarabi p:nth-child(26)').style.display = "block";
        
    };
}
let selectThumQ16 = document.querySelector('[name="thumbnailQ16"]');
selectThumQ16.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ16.value != ''){
        document.querySelector('.yokonarabi p:nth-child(27)').style.display = "block";
        
    };
}
let selectThumQ17 = document.querySelector('[name="thumbnailQ17"]');
selectThumQ17.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ17.value != ''){
        document.querySelector('.yokonarabi p:nth-child(28)').style.display = "block";
        
    };
}
let selectThumQ18 = document.querySelector('[name="thumbnailQ18"]');
selectThumQ18.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ18.value != ''){
        document.querySelector('.yokonarabi p:nth-child(29)').style.display = "block";
        
    };
}
let selectThumQ19 = document.querySelector('[name="thumbnailQ19"]');
selectThumQ19.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ19.value != ''){
        document.querySelector('.yokonarabi p:nth-child(30)').style.display = "block";
        
    };
}
let selectThumQ20 = document.querySelector('[name="thumbnailQ20"]');
selectThumQ20.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ20.value != ''){
        document.querySelector('.yokonarabi p:nth-child(31)').style.display = "block";
        
    };
}
let selectThumQ21 = document.querySelector('[name="thumbnailQ21"]');
selectThumQ21.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ21.value != ''){
        document.querySelector('.yokonarabi p:nth-child(32)').style.display = "block";
        
    };
}
let selectThumQ22 = document.querySelector('[name="thumbnailQ22"]');
selectThumQ22.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ22.value != ''){
        document.querySelector('.yokonarabi p:nth-child(33)').style.display = "block";
        
    };
}
let selectThumQ23 = document.querySelector('[name="thumbnailQ23"]');
selectThumQ23.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ23.value != ''){
        document.querySelector('.yokonarabi p:nth-child(34)').style.display = "block";
        
    };
}
let selectThumQ24 = document.querySelector('[name="thumbnailQ24"]');
selectThumQ24.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ24.value != ''){
        document.querySelector('.yokonarabi p:nth-child(35)').style.display = "block";
        
    };
}
let selectThumQ25 = document.querySelector('[name="thumbnailQ25"]');
selectThumQ25.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ25.value != ''){
        document.querySelector('.yokonarabi p:nth-child(36)').style.display = "block";
        
    };
}
let selectThumQ26 = document.querySelector('[name="thumbnailQ26"]');
selectThumQ26.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ26.value != ''){
        document.querySelector('.yokonarabi p:nth-child(37)').style.display = "block";
        
    };
}
let selectThumQ27 = document.querySelector('[name="thumbnailQ27"]');
selectThumQ27.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ27.value != ''){
        document.querySelector('.yokonarabi p:nth-child(38)').style.display = "block";
        
    };
}
let selectThumQ28 = document.querySelector('[name="thumbnailQ28"]');
selectThumQ28.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ28.value != ''){
        document.querySelector('.yokonarabi p:nth-child(39)').style.display = "block";
        
    };
}
let selectThumQ29 = document.querySelector('[name="thumbnailQ29"]');
selectThumQ29.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumQ29.value != ''){
        document.querySelector('.yokonarabi p:nth-child(40)').style.display = "block";
        
    };
}


// 1/21
let selectAnswerTitle1 = document.querySelector('[name="answerTitle1"]');
let selectAnswer1 = document.querySelector('[name="answer1"]');
selectAnswerTitle1.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswerTitle1.value != ''){
        document.querySelector('.yokonarabi p:nth-child(44)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(45)').style.display = "block";
    };
}
selectAnswer1.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswer1.value != ''){
        document.querySelector('.yokonarabi p:nth-child(44)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(45)').style.display = "block";
    };
}


let selectAnswerTitle2 = document.querySelector('[name="answerTitle2"]');
let selectAnswer2 = document.querySelector('[name="answer2"]');
selectAnswerTitle2.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswerTitle2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(46)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(47)').style.display = "block";
    };
}
selectAnswer2.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswer2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(46)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(47)').style.display = "block";
    };
}


let selectAnswerTitle3 = document.querySelector('[name="answerTitle3"]');
let selectAnswer3 = document.querySelector('[name="answer3"]');
selectAnswerTitle3.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswerTitle3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(48)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(49)').style.display = "block";
    };
}
selectAnswer3.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswer3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(48)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(49)').style.display = "block";
    };
}



let selectAnswerTitle4 = document.querySelector('[name="answerTitle4"]');
let selectAnswer4 = document.querySelector('[name="answer4"]');
selectAnswerTitle4.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswerTitle4.value != ''){
        document.querySelector('.yokonarabi p:nth-child(50)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(51)').style.display = "block";
    };
}
selectAnswer4.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectAnswer4.value != ''){
        document.querySelector('.yokonarabi p:nth-child(50)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(51)').style.display = "block";
    };
}











let selectThumbA1 = document.querySelector('[name="thumbnailA1"]');
selectThumbA1.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumbA1.value != ''){
        document.querySelector('.yokonarabi p:nth-child(53)').style.display = "block";
        
    };
}
let selectThumbA2 = document.querySelector('[name="thumbnailA2"]');
selectThumbA2.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumbA2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(54)').style.display = "block";
        
    };
}
let selectThumbA3 = document.querySelector('[name="thumbnailA3"]');
selectThumbA3.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumbA3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(55)').style.display = "block";
        
    };
}
let selectThumbA4 = document.querySelector('[name="thumbnailA4"]');
selectThumbA4.onchange = event => { 
    /*最初非表示から表示 */  
    if(selectThumbA4.value != ''){
        document.querySelector('.yokonarabi p:nth-child(56)').style.display = "block";
        
    };
}