# Распознавание изображения по форме
Программа по распознаванию изображений по их геометрической форме. 
Определение изображения происходит путем перевода в формат полутонов и наложения фильтра Щарра для определения границ. Алгоритм определения заключается в рассмотрении расстояния до контура объектов.

## Выделение контура
Алгоритм распознавания изображения по форме основан на методе выделения контура путем вычисления значения яркости по координатам изображения. Для успешного выделения контура предполагается, что яркость объекта и фона существенно отличаются друг от друга. Для более точного определения изображения используются различные операторы выделения границ. Фильтры, выделяющие контурные линии, можно отнести к высокочастотным фильтрам, т.е. подавляющим низкочастотную составляющую изображения. Теоретически на результирующем изображении яркость должна быть отлична от нуля только у пикселей, входящих в контурную линию, однако из-за наличия шумовых помех такого эффекта удается достичь не всегда.

### Оператор Щарра
> Большим недостатком других операторов (особенно Собеля) является отсутствие полной вращательной симметрии. Оператор Щарра существенно снижает отрицательные эффекты за счет использования измененных ядер свертки. Данный оператор более чувствителен при извлечении границы и способен извлекать меньшие границы. Однако отсюда повышается вероятность ошибки, поэтому большая чувствительность может быть рискованной.

![image](https://user-images.githubusercontent.com/108347547/180743585-acde7a3b-4989-46df-b6b5-dc42a897b23d.png)

