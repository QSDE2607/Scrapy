<h1> Xây dựng hệ thống thu thập dữ liệu Covid 19 </h1>

<h2> Tổng quan dự án </h2>

Ở bài ASM này, bạn sẽ cần xây dựng hệ thống thu thập dữ liệu số ca nhiễm Covid 19 ở VIệt Nam qua từng ngày khác nhau.
<ol>
<li>Xây dựng được Spider để tải và bóc tách các dữ liệu cần thiết. </li>
<li>Sử dụng Spider để xử lý việc chuyển trang web để lấy được các dữ liệu từ ngày cũ hơn.</li>
<li>Lấy được dữ liệu về ngày tháng và số ca nhiễm mới vào ngày đó.</li>
<li> Lưu các dữ liệu thu thập được dưới dạng .json </li>
</ol>

<h2> Yêu cầu dự án </h2>

<h3> 1. Xây dựng được Spider để tải và bóc tách các dữ liệu cần thiết. </h3>

Đầu tiên bạn cần tạo một Project Scrapy mới thông qua hàm startproject. Sau đó là tạo một Spider mới để bắt đầu thu thập dữ liệu.

<h3> 2. Sử dụng Spider để xử lý việc chuyển trang web để lấy được các dữ liệu từ ngày cũ hơn. </h3>

Ở cuối trang, bạn sẽ thấy các nút để chuyển trang như sau:

![image](https://github.com/QSDE2607/Scrapy/assets/171625181/0238eeff-1bf9-4747-9070-babc9d4347c4)


Ở mỗi nút sẽ chứa link đến trang web tiếp theo. Bạn cần truy vấn phần tử và lấy được link đó. Sau đó sẽ tiếp tục gửi request và xử lý cho link tiếp theo.

<h3> 3. Lấy được dữ liệu về ngày tháng và số ca nhiễm mới vào ngày đó. </h3>

Mỗi một mục sẽ có dạng như sau:

![image](https://github.com/QSDE2607/Scrapy/assets/171625181/a3224c52-433b-4197-9b7d-87e7c97993c0)


Bạn sẽ cần truy vấn các phần tử để lấy các thông tin về thời gian cũng như số ca mắc mới. Ở ví dụ trên thì bạn cần lấy các thông tin như sau:

Thời gian: “06:00 12/08/2021”
Số ca mắc mới: “THÔNG BÁO VỀ 4.642 CA MẮC MỚI ”
Về cách lấy dữ liệu về số ca mắc mới, bạn có thể sử dụng regex để tách các số, hoặc sử dụng các biện pháp cắt chuỗi, thay thế chuỗi để xử lý. Sau khi xử lý thành công thì ta sẽ được dữ liệu ở dạng sau:

![image](https://github.com/QSDE2607/Scrapy/assets/171625181/6b432834-24f7-40f9-86ef-710846b26388)


<h3>  4. Lưu các dữ liệu thu thập được dưới dạng .json </h3>

Sau khi trích xuất và xử lý thành công, bạn cần lưu các dữ liệu đó ở dạng file .json, file đó sẽ có cấu trúc như sau:

![image](https://github.com/QSDE2607/Scrapy/assets/171625181/813af95f-50bb-443d-9925-e7acdb78f6c1)


Lưu ý: Do một số mục có thông tin không đồng nhất với nhau, bạn có thể skip qua các mục này và chỉ xử lý các mục có số liệu rõ ràng về các ca mắc mới.

<h3>  5. (Yêu cầu nâng cao) Trích xuất được các dữ liệu về số ca nhiễm mới của từng thành phố.</h3>

Với yêu cầu nâng cao này, bạn sẽ cần trích xuất số liệu để biết được mỗi thành phố có bao nhiêu ca nhiễm mới. Các dữ liệu này sẽ có dạng như sau:

![image](https://github.com/QSDE2607/Scrapy/assets/171625181/f9b53289-5752-420f-93b0-7b7419f5ecb6)


Bạn sẽ cần trích xuất các thông tin như sau:

![image](https://github.com/QSDE2607/Scrapy/assets/171625181/aabfb3ce-a291-4681-970a-2e93865baa49)


Để làm được yêu cầu này,  bạn có thể sử dụng regex để tách các số, hoặc sử dụng các biện pháp cắt chuỗi, thay thế chuỗi để xử lý.

Lưu ý: Do một số mục có thông tin không đồng nhất với nhau, bạn có thể skip qua các mục này và chỉ xử lý các mục có số liệu rõ ràng về các ca mắc mới của từng thành phố.

Ngoài ra, để xử lý dữ liệu dễ hơn. Bạn nên xóa bỏ hết các dấu tiếng Việt ở trong chuỗi bạn cần xây dựng hàm để xử lý việc này
