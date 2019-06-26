## Linear search algorithm (線形探索アルゴリズム)

説明：ソートされてないリストで最初から最後まで一つずつ順番で検査し、望む値を探すアルゴリズム



```php
<?php 
/**
 * Linear search algorithm
 *
 * @param array $list
 * @param int $searchValue
 *
 * @return  bool
 */
function hasSearchValueByLinearSearchAlgorithm (array $list, $searchValue) {
    for ($i = 0 ; $i < count($list) ; $i++) {
        if ($list[$i] === $searchValue) {
            return true;
        }
    }

    return false;
}

$list = [1, 50, 30, 20, 5, 40, 10,];
$searchValue = rand(0, 50);

if (hasSearchValueByLinearSearchAlgorithm($list, $searchValue)) {
    echo "探す値があります！!";
} else {
    echo "探す値がありません！!";
}
?>
```

## 

## Linear search algorithm (순차 탐색 알고리즘)

설명 : 정렬되지 않은 리스트에서 맨 앞부터 마지막까지 차례대로 하나씩 검사하여 원하는 항목을 찾아가는 알고리즘.



```php
<?php 
    
/**
 * Linear search algorithm
 *
 * @param array $list
 * @param int $searchValue
 *
 * @return  bool
 */
function hasSearchValueByLinearSearchAlgorithm (array $list, $searchValue) {
    for ($i = 0 ; $i < count($list) ; $i++) {
        if ($list[$i] === $searchValue) {
            return true;
        }
    }

    return false;
}

$list = [1, 50, 30, 20, 5, 40, 10,];
$searchValue = rand(0, 50);

if (hasSearchValueByLinearSearchAlgorithm($list, $searchValue)) {
    echo " 찾는 값이 있어요!";
} else {
    echo "찾는 값이 없어요!";
}
?>
```

## 