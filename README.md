# Dataset Editing Pipeline

Этот pipeline позволяет автоматически аугментировать данные с помощью диффузионных моделей, создавая новые фоны, изменяя положение объекта на изображении, его размер и угол.

## Использование

Файл `app.ipynb` содержит полный цикл работы бенчмарка. Последовательный запуск ячеек позволит увидеть, как он работает на примере датасета с птицами.

## Установка и запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустите `app.ipynb` в Jupyter Notebook.

## Примеры изображений

Первая строка таблицы демонстрирует оригинальные изображения взятых из набора данных про птиц.
Вторая и третья строка это сгенерированные данные полученные с помощью этого пайплайна, где задействованы все возможности в видеизменений: фона, угла поворота, размера объекта.
<table>
  <tr>
    <td><img src="images/albatross_orig.jpg" alt="Albatross Original" width="100%"></td>
    <td><img src="images/bananaquit_orig.jpg" alt="Bananaquit Original" width="100%"></td>
    <td><img src="images/bobolink_orig.jpg" alt="Bobolink Original" width="100%"></td>
    <td><img src="images/gyfralcon_orig.jpg" alt="Gyfralcon Original" width="100%"></td>
    <td><img src="images/sora_orig.jpg" alt="Sora Original" width="100%"></td>
  </tr>
  <tr>
    <td><img src="images/albatross_1.jpg" alt="Albatross 1" width="100%"></td>
    <td><img src="images/bananaquit_1.jpg" alt="Bananaquit 1" width="100%"></td>
    <td><img src="images/bobolink_1.jpg" alt="Bobolink 1" width="100%"></td>
    <td><img src="images/gyfralcon_1.jpg" alt="Gyfralcon 1" width="100%"></td>
    <td><img src="images/sora_1.jpg" alt="Sora 1" width="100%"></td>
  </tr>
  <tr>
    <td><img src="images/albatross_2.jpg" alt="Albatross 2" width="100%"></td>
    <td><img src="images/bananaquit_2.jpg" alt="Bananaquit 2" width="100%"></td>
    <td><img src="images/bobolink_2.jpg" alt="Bobolink 2" width="100%"></td>
    <td><img src="images/gyfralcon_2.jpg" alt="Gyfralcon 2" width="100%"></td>
    <td><img src="images/sora_2.jpg" alt="Sora 2" width="100%"></td>
  </tr>
</table>