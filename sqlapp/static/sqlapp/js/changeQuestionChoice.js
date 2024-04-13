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

// window.onloadを使用して、すべてのリソースがロードされた後に関数を実行
window.onload = function() {
    checkAndApplyStyleThumbQ1();
    checkAndApplyStyleThumbQ2();
    checkAndApplyStyleThumbA1();
    checkAndApplyStyleThumbA2();
};

let select2 = document.querySelector('[name="thumbnailQ1"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleThumbQ1() {
    // 既存のファイルのリンクがあるか、新しいファイルが選択されているかチェック
    if (select2.value != '') {
        document.querySelector('.yokonarabi p:nth-child(7)').style.display = "block";
    } else {
        document.querySelector('.yokonarabi p:nth-child(7)').style.display = "none";
    }
}

// ファイル選択時にも同じ関数を実行
select2.addEventListener('change', checkAndApplyStyleThumbQ1);




let select22 = document.querySelector('[name="thumbnailQ2"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleThumbQ2() {
    if(select22.value != ''){
        document.querySelector('.yokonarabi p:nth-child(8)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(8)').style.display = "none";
    }
}
// 入力時にも同じ関数を実行
select22.addEventListener('change', checkAndApplyStyleThumbQ2);



/*
let select3 = document.querySelector('[name="wronganswer3"]');
select3.addEventListener('input', event => { 
    if(select3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(13) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(13)').style.display = "none";
    }
});
*/



let select3 = document.querySelector('[name="wronganswer3"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleWrong3() {
    if(select3.value != ''){
        document.querySelector('.yokonarabi p:nth-child(13) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(13)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(13)').style.display = "none";
    }
}
// ページロード時に関数を実行
document.addEventListener('DOMContentLoaded', function() {
    checkAndApplyStyleWrong3();
});
// 入力時にも同じ関数を実行
select3.addEventListener('input', checkAndApplyStyleWrong3);






let select4 = document.querySelector('[name="wronganswer4"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleWrong4() {
    if(select4.value != ''){
        document.querySelector('.yokonarabi p:nth-child(14) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(14)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(14)').style.display = "none";
    }
}
// ページロード時に関数を実行
document.addEventListener('DOMContentLoaded', function() {
    checkAndApplyStyleWrong4();
});
// 入力時にも同じ関数を実行
select4.addEventListener('input', checkAndApplyStyleWrong4);



let select5 = document.querySelector('[name="wronganswer5"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleWrong5() {
    if(select5.value != ''){
        document.querySelector('.yokonarabi p:nth-child(15) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(15)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(15)').style.display = "none";
    }
}
// ページロード時に関数を実行
document.addEventListener('DOMContentLoaded', function() {
    checkAndApplyStyleWrong5();
});
// 入力時にも同じ関数を実行
select5.addEventListener('input', checkAndApplyStyleWrong5);


let select6 = document.querySelector('[name="wronganswer6"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleWrong6() {
    if(select6.value != ''){
        document.querySelector('.yokonarabi p:nth-child(16) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(16)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(16)').style.display = "none";
    }
}
// ページロード時に関数を実行
document.addEventListener('DOMContentLoaded', function() {
    checkAndApplyStyleWrong6();
});
// 入力時にも同じ関数を実行
select6.addEventListener('input', checkAndApplyStyleWrong6);

let select7 = document.querySelector('[name="wronganswer7"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleWrong7() {
    if(select7.value != ''){
        document.querySelector('.yokonarabi p:nth-child(17) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(17)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(17)').style.display = "none";
    }
}
// ページロード時に関数を実行
document.addEventListener('DOMContentLoaded', function() {
    checkAndApplyStyleWrong7();
});
// 入力時にも同じ関数を実行
select7.addEventListener('input', checkAndApplyStyleWrong7);


let select8 = document.querySelector('[name="wronganswer8"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleWrong8() {
    if(select8.value != ''){
        document.querySelector('.yokonarabi p:nth-child(18) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(18)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(18)').style.display = "none";
    }
}
// ページロード時に関数を実行
document.addEventListener('DOMContentLoaded', function() {
    checkAndApplyStyleWrong3();
});
// 入力時にも同じ関数を実行
select8.addEventListener('input', checkAndApplyStyleWrong8);


let select10 = document.querySelector('[name="hint1"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleHint1() {
    if(select10.value != ''){
        document.querySelector('.yokonarabi p:nth-child(20) textarea').style.height = "28.24px";
        document.querySelector('.yokonarabi p:nth-child(20)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(20)').style.display = "none";
    }
}
// ページロード時に関数を実行
document.addEventListener('DOMContentLoaded', function() {
    checkAndApplyStyleHint1();
});
// 入力時にも同じ関数を実行
select10.addEventListener('input', checkAndApplyStyleHint1);



let select23 = document.querySelector('[name="thumbnailA1"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleThumbA1() {
    if(select23.value != ''){
        document.querySelector('.yokonarabi p:nth-child(25)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(25)').style.display = "none";
    }
}
// 入力時にも同じ関数を実行
select23.addEventListener('change', checkAndApplyStyleThumbA1);


let select24 = document.querySelector('[name="thumbnailA2"]');
// 条件をチェックし、スタイルを適用する関数
function checkAndApplyStyleThumbA2() {
    if(select24.value != ''){
        document.querySelector('.yokonarabi p:nth-child(26)').style.display = "block";
    }
    else {
        document.querySelector('.yokonarabi p:nth-child(26)').style.display = "none";
    }
}
// 入力時にも同じ関数を実行
select24.addEventListener('change', checkAndApplyStyleThumbA2);