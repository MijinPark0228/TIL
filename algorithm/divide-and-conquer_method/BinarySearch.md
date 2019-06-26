## Binary search algorithm (二分探索)

#### 説明

- ソートされた状態で与えられた元素を半分ずつ減らして、望む値を探す

  探索を実行するたびに、探索の対象になる元素数が1/2になる。

- ソートされたリストだけに適用が可能なアルゴリズム。

  元素を追加・削除の時にはソートの状態を保つため、元素を移動が発生する。

  そのため、追加・削除の演算が頻繁に行う場合は不適切である。

  

#### 性能 

`T(n)=T(n/2)+Θ(1), T(1)=Θ(1) → Θ(logn)`



#### 再帰関数を利用

```php
/**
 * 再帰関数を利用する.
 *
 * @param array $list
 * @param int $leftIndex
 * @param int $rightIndex
 * @param int $searchValue
 *
 * @return bool|int
 */
function binarySearchByRecursiveCall(array $list, $leftIndex, $rightIndex, $searchValue)
{
    if ($leftIndex > $rightIndex) {
        return false;
    }

    $mid = floor((($leftIndex+$rightIndex)/2));
    if ($searchValue === $list[$mid]) {
        return $mid;
    }

    if ($searchValue < $mid) {
        $rightIndex = $mid-1;
    } else {
        $leftIndex = $mid+1;
    }

    return binarySearchByRecursiveCall($list, $leftIndex, $rightIndex, $searchValue);
}

$list = [1,2,3,5,6,7,8,9,10];

$searchValue = 4;

$searchIndex = binarySearchByRecursiveCall($list, 0, count($list)-1, $searchValue);
if ($searchValue === false) {
    echo "値がありませんよー!";
} else {
    echo "探す値のindex位置は".$searchIndex;
}
```



#### 繰り返し文を利用

```php
/**
 * 繰り返し文を利用する.
 *
 * @param array $list
 * @param int $searchValue
 *
 * @return int
 */
function binarySearchByIteration(array $list, $searchValue)
{
    $leftIndex = 0;
    $rightIndex = count($list);

    while ($leftIndex <= $rightIndex) {
        $mid = floor((($leftIndex+$rightIndex) / 2));
        if ( $searchValue === $list[$mid] ) {
            return $mid;
        }

        if ($searchValue < $mid) {
            $rightIndex = $mid-1;
        } else {
            $leftIndex = $mid+1;
        }
    }

    return false;
}


$list = [1,2,3,5,6,7,8,9,10];

$searchValue = 9;

$searchIndex = binarySearchByIteration($list, $searchValue);
if ($searchValue === false) {
    echo "値がありませんよー!";
} else {
    echo "探す値のindex位置は".$searchIndex;
}
```



------




## Binary search algorithm (이진탐색)

#### 설명

- 정렬된 상태로 주어진 원소들을 절반씩 줄여가면서 원하는 키값을 찾는 문제

​			탐색을 수행할 때마다 탐색 대상이 되는 원소의 개수가 1/2씩 감소

- 정렬된 리스트에 대해서만 적용 가능하다.

  삽입/삭제 시 정렬 상태의 유지를 위해 원소의 이동이 발생하기 때문에 삽입/삭제 연산이 빈번한 응용에는 부적합

  

#### 성능

`T(n)=T(n/2)+Θ(1), T(1)=Θ(1) → Θ(logn)`



#### 재귀함수 이용

```php
/**
 * 재귀함수 이용.
 *
 * @param array $list
 * @param int $leftIndex
 * @param int $rightIndex
 * @param int $searchValue
 *
 * @return bool|int
 */
function binarySearchByRecursiveCall(array $list, $leftIndex, $rightIndex, $searchValue)
{
    if ($leftIndex > $rightIndex) {
        return false;
    }

    $mid = floor((($leftIndex+$rightIndex)/2));
    if ($searchValue === $list[$mid]) {
        return $mid;
    }

    if ($searchValue < $mid) {
        $rightIndex = $mid-1;
    } else {
        $leftIndex = $mid+1;
    }

    return binarySearchByRecursiveCall($list, $leftIndex, $rightIndex, $searchValue);
}

$list = [1,2,3,5,6,7,8,9,10];

$searchValue = 4;

$searchIndex = binarySearchByRecursiveCall($list, 0, count($list)-1, $searchValue);
if ($searchValue === false) {
    echo "찾는 값이 없음";
} else {
    echo "찾는 값의 위치는 ".$searchIndex;
}
```



#### 반복문 이용

```php
/**
 * 반복문 이용.
 *
 * @param array $list
 * @param int $searchValue
 *
 * @return int
 */
function binarySearchByIteration(array $list, $searchValue)
{
    $leftIndex = 0;
    $rightIndex = count($list);

    while ($leftIndex <= $rightIndex) {
        $mid = floor((($leftIndex+$rightIndex) / 2));
        if ( $searchValue === $list[$mid] ) {
            return $mid;
        }

        if ($searchValue < $mid) {
            $rightIndex = $mid-1;
        } else {
            $leftIndex = $mid+1;
        }
    }

    return false;
}


$list = [1,2,3,5,6,7,8,9,10];

$searchValue = 9;

$searchIndex = binarySearchByIteration($list, $searchValue);
if ($searchValue === false) {
    echo "찾는 값이 없음!";
} else {
    echo "찾는 값의 위치는 ".$searchIndex;
}
```



