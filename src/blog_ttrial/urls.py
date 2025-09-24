from django.contrib import admin
from django.urls import path,include
from blog_ttrial.views import *

urlpatterns = [
   path('blog_pg1/',blogApp_page1, name="blog_pg1"),
   path('blog_pg2/',blogApp_page2, name="blog_pg2"),
   path('blog_pg3/',blogApp_page3, name="blog_pg3"),
   path('blog_pg4/',blogApp_page4, name="blog_pg4"),
   path('blog_pg5/',blogApp_page5, name="blog_pg5"),
   path('blog_pg6/',blogApp_page6, name="blog_pg6"),
   path('blog_pg7/',blogApp_page7, name="blog_pg7"),
   path('blog_pg8/',blogApp_page8, name="blog_pg8"),
   path('blog_pg9/',blogApp_page9, name="blog_pg9"),
   path('blog_pg10/',blogApp_page10, name="blog_pg10"),
   path('blog_pg11/',blogApp_page11, name="blog_pg11"),
   path('blog_pg12/',blogApp_page12, name="blog_pg12"),
   path('blog_pg13/',blogApp_page13, name="blog_pg13"),
   path('blog_pg14/',blogApp_page14, name="blog_pg14"),
   path('blog_pg15/',blogApp_page15, name="blog_pg15"),
   path('blog_pg16/',blogApp_page16, name="blog_pg16"),
   path('blog_pg17/',blogApp_page17, name="blog_pg17"),
   path('blog_pg18/',blogApp_page18, name="blog_pg18"),
   path('blog_pg19/',blogApp_page19, name="blog_pg19"),
   path('blog_pg20/',blogApp_page20, name="blog_pg20"),
   path('blog_pg21/',blogApp_page21, name="blog_pg21"),
   path('blog_pg22/',blogApp_page22, name="blog_pg22"),
   path('blog_pg23/',blogApp_page23, name="blog_pg23"),
   path('blog_pg24/',blogApp_page24, name="blog_pg24"),
   path('blog_pg25/',blogApp_page25, name="blog_pg25"),
   path('blog_pg26/',blogApp_page26, name="blog_pg26"),
   path('blog_pg26_b/',blogApp_page26_b, name="blog_pg26_b"),
   #Exercise Two submissions
   path('blog_ex2_submission/',blog_ex2_submission, name="blog_ex2_submission"),
   path('blog_ex2_SuccessView/', blog_ex2_SuccessView, name="blog_ex2_SuccessView"),

   path('blog_pg27/',blogApp_page27, name="blog_pg27"),
   path('blog_pg27_b/',blogApp_page27_b, name="blog_pg27_b"),
   path('blog_pg28/',blogApp_page28, name="blog_pg28"),
   path('blog_pg29/',blogApp_page29, name="blog_pg29"),
   path('blog_pg30/',blogApp_page30, name="blog_pg30"),
   path('blog_pg31/',blogApp_page31, name="blog_pg31"),
   path('blog_pg32/',blogApp_page32, name="blog_pg32"),
   path('blog_pg33/',blogApp_page33, name="blog_pg33"),
   path('blog_pg34/',blogApp_page34, name="blog_pg34"),
   path('blog_pg35/',blogApp_page35, name="blog_pg35"),
   path('blog_pg36/',blogApp_page36, name="blog_pg36"),
   path('blog_pg37/',blogApp_page37, name="blog_pg37"),
   path('blog_pg38/',blogApp_page38, name="blog_pg38"),
   path('blog_pg39/',blogApp_page39, name="blog_pg39"),
   #Exercise Three submissions
   path('blog_ex3_submission/',blog_ex3_submission, name="blog_ex3_submission"),
   path('blog_ex3_SuccessView/', blog_ex3_SuccessView, name="blog_ex3_SuccessView"),

   path('blog_pg40/',blogApp_page40, name="blog_pg40"),
   path('blog_pg40_b/',blogApp_page40_b, name="blog_pg40_b"),
   path('blog_pg41/',blogApp_page41, name="blog_pg41"),
   path('blog_pg42/',blogApp_page42, name="blog_pg42"),
   path('blog_pg43/',blogApp_page43, name="blog_pg43"),
   path('blog_pg44/',blogApp_page44, name="blog_pg44"),
   path('blog_pg45/',blogApp_page45, name="blog_pg45"),
   path('blog_pg46/',blogApp_page46, name="blog_pg46"),
   path('blog_pg47/',blogApp_page47, name="blog_pg47"),
   path('blog_pg48/',blogApp_page48, name="blog_pg48"),
   path('blog_pg49/',blogApp_page49, name="blog_pg49"),
   path('blog_pg50/',blogApp_page50, name="blog_pg50"),
   path('blog_pg51/',blogApp_page51, name="blog_pg51"),
   path('blog_pg52/',blogApp_page52, name="blog_pg52"),
   path('blog_pg53/',blogApp_page53, name="blog_pg53"),
   path('blog_pg54/',blogApp_page54, name="blog_pg54"),
   path('blog_pg55/',blogApp_page55, name="blog_pg55"),
   path('blog_pg56/',blogApp_page56, name="blog_pg56"),
   path('blog_pg57/',blogApp_page57, name="blog_pg57"),
   path('blog_pg58/',blogApp_page58, name="blog_pg58"),
   path('blog_pg59/',blogApp_page59, name="blog_pg59"),
   path('blog_pg59_b/',blogApp_page59_b, name="blog_pg59_b"),
   #Exercise Four submissions
   path('blog_ex4_submission/',blog_ex4_submission, name="blog_ex4_submission"),
   path('blog_ex4_SuccessView/', blog_ex4_SuccessView, name="blog_ex4_SuccessView"),

   path('blog_pg60/',blogApp_page60, name="blog_pg60"),


#    blog_preview
   path('blogPreview_home/',blogPreview_index, name="blogPreview_home"), 
   path('blogPreview_trends/',blogPreview_trends, name="blogPreview_trends"), 
   path('blogPreview_designers/',blogPreview_designers, name="blogPreview_designers"),
   path('blogPreview_outfits/',blogPreview_outfits, name="blogPreview_outfits"),
   path('blogPreview_beauty/',blogPreview_beauty, name="blogPreview_beauty"),
   path('blogPreview_about/',blogPreview_about, name="blogPreview_about"),
   path('blogPreview_contact/',blogPreview_contact, name="blogPreview_contact"),


# break messages
   path('congrats/',congrats, name="congrats"),
    
    
]