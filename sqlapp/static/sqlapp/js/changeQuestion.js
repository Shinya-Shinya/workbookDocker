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
let select2 = document.querySelector('[name="thumbnailQ1"]');
select2.onchange = event => { 
    /*最初非表示から表示 */  
    if(select2.value != ''){
        document.querySelector('.yokonarabi p:nth-child(7)').style.display = "block";
        
    };
}
let select22= document.querySelector('[name="thumbnailQ2"]');
select22.onchange = event => { 
    /*最初非表示から表示 */  
    if(select22.value != ''){
        document.querySelector('.yokonarabi p:nth-child(8)').style.display = "block";
        
    };
}
let select3 = document.querySelector('[name="wronganswer3"]');
select3.onchange = event => { 
    /*最初非表示から表示 */  
    if(select3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
        
    };
}
let select4 = document.querySelector('[name="wronganswer4"]');
select4.onchange = event => { 
    /*最初非表示から表示 */  
    if(select4.value != ''){
        document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
        
    };
}
let select5 = document.querySelector('[name="wronganswer5"]');
select5.onchange = event => { 
    /*最初非表示から表示 */  
    if(select5.value != ''){
        document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
        
    };
}
let select6 = document.querySelector('[name="wronganswer6"]');
select6.onchange = event => { 
    /*最初非表示から表示 */  
    if(select6.value != ''){
        document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
        
    };
}
let select7 = document.querySelector('[name="wronganswer7"]');
select7.onchange = event => { 
    /*最初非表示から表示 */  
    if(select7.value != ''){
        document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
        
    };
}
let select8 = document.querySelector('[name="wronganswer8"]');
select8.onchange = event => { 
    /*最初非表示から表示 */  
    if(select8.value != ''){
        document.querySelector('.yokonarabi p:nth-child(18)').style.display = "block";
        
    };
}
let select9 = document.querySelector('[name="wronganswer9"]');
select9.onchange = event => { 
    /*最初非表示から表示 */  
    if(select9.value != ''){
        document.querySelector('.yokonarabi p:nth-child(19)').style.display = "block";
        
    };
}
let select10 = document.querySelector('[name="hint1"]');
select10.onchange = event => { 
    /*最初非表示から表示 */  
    if(select10.value != ''){
        document.querySelector('.yokonarabi p:nth-child(20)').style.display = "block";
        document.querySelector('.yokonarabi p:nth-child(20)').style.height = "28.24px !important";
        
    };
}
let select23 = document.querySelector('[name="thumbnailA1"]');
select23.onchange = event => { 
    /*最初非表示から表示 */  
    if(select23.value != ''){
        document.querySelector('.yokonarabi p:nth-child(25)').style.display = "block";
        
    };
}
let select24 = document.querySelector('[name="thumbnailA2"]');
select24.onchange = event => {
    /*最初非表示から表示 */  
    if(select24.value != ''){
        document.querySelector('.yokonarabi p:nth-child(26)').style.display = "block";
    };
}