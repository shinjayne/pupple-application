from django.db import models

from accounts.models import IPUserProfile

ITEM_CATEGORY = [('T-shirts', '티셔츠'), ('Hoodie/Sweat shirts', '후드/집업/맨투맨'), ('Shirts/Blouse', '셔츠/블라우스'), ('Knite/Cardigan', '니트/가디건'), ('Outer', '아우터'), ('Pants', '팬츠'), ('Skirt', '스커트'), ('One-piece', '원피스'), ('Sports', '스포츠'), ('Underwear', '언더웨어'), ('Bag', '가방'), ('Wallet/Pouch', '지갑/파우치'), ('Watch', '시계'), ('Hat', '모자'), ('Glass/Sunglass', '안경/선글라스'), ('Jewelry', '쥬얼리'), ('Shocks', '양말/스타킹'), ('Sneakers', '스니커즈'), ('Shoes', '구두'), ('Sandal', '샌들'), ('Boots', '부츠'), ('Shoe care', '슈케어'), ('Men shoes', '남성슈즈'), ('Phone accessories', '휴대폰 액세서리'), ('etc', '기타')]

# def item_img_upload_path(instance):
#     return "contents/item/{}".format(instance.item.name)

# def look_img_upload_path(instance):
#     return "contents/look/{}".format(instance.look.title)

class ShoppableContents(models.Model):
    title = models.CharField(max_length=100)
    explain = models.TextField(blank=True)  ## max_length 지정할지 고민
    background_img = models.ImageField(upload_to="contents/shoppable/background", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '퍼플 컨텐츠'
        verbose_name_plural = '퍼플 컨텐츠들'

    def __str__(self):
        return self.title

class Creator(models.Model):
    name = models.CharField(max_length=20)
    explain = models.TextField(blank=True)  ## max_length 지정할지 고민
    profile_img = models.ImageField(upload_to="contents/creator/profile", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class YoutubeContents(models.Model):
    shoppable_contents = models.ForeignKey(ShoppableContents, on_delete=models.SET_NULL, null=True, related_name="youtube_contents_set")
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    link = models.URLField()

    class Meta:
        verbose_name = '유튜브 컨텐츠 정보'
        verbose_name_plural = '유튜브 컨텐츠 정보들'


    def __str__(self):
        return self.title

class ItemTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=ITEM_CATEGORY, default='none' , max_length=50)
    main_img = models.ImageField(upload_to="contents/item/{}".format(name), blank=True)
    # imgs = models.ForeignKey('ItemImage', on_delete=models.SET_NULL, null=True)
    explain = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    link = models.URLField(blank=True, help_text='https 로 접속 가능하면 https 로 해주세요.')
    tags = models.ManyToManyField(ItemTag, blank=True)
    hit = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품들'

    def __str__(self):
        return f"[{self.category}] {self.name} (W {self.price})"

# class ItemImage(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to=item_img_upload_path)

class Look(models.Model):
    youtube_contents = models.ForeignKey(YoutubeContents, on_delete=models.SET_NULL, null=True, related_name="look_set")
    title = models.CharField(max_length=100)
    main_img = models.ImageField(upload_to="contents/look/{}".format(title), blank=True)
    main_img_aspect_ratio = models.FloatField(default=1.0, db_column='main_img_aspect_ratio', verbose_name='가로/세로비', help_text="가로길이 나누기 세로길이. 정방형이면 1.")
    # imgs = models.ForeignKey('LookImage', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(Item)
    like = models.PositiveIntegerField(default=0)
    liked_users = models.ManyToManyField(IPUserProfile, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '장면'
        verbose_name_plural = '장면들'

    def __str__(self):
        return "[" + self.youtube_contents.title[:20] + "...] " + self.title

# class LookImage(models.Model):
#     look = models.ForeignKey(Look, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to=look_img_upload_path)

