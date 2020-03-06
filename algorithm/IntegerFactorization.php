<?php
/*素因数分解 (소인수분해)*/
function printNumberFactorizer($number)
{
    $sortList = [];
    $p = 2;

    while ($number != 1) {
        if ($number % $p === 0) {
            $sortList[$p] = true;
            $number = $number / $p;
        } else {
            $p++;
        }
    }

    foreach ($sortList as $key => $value) {
        echo $key.PHP_EOL;
    }
}

$testValue = 26
printNumberFactorizer($testValue);
