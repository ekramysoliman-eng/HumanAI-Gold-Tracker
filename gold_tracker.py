from scrapling import fetchers
import time

def get_live_gold():
    # تفعيل وضع التخفي والتكيف
    fetcher = fetchers.StealthyFetcher()
    fetcher.adaptive = True 
    
    # سنستهدف موقع 'isagha' كمثال حي
    url = "https://www.isagha.com/gold-prices"
    
    print("🔍 جاري سحب البيانات كشبح...")
    page = fetcher.fetch(url)
    
    # ملاحظة: الـ Selector أدناه يحتاج لتأكيد من هيكل الموقع لحظة التشغيل
    # Scrapling سيتكفل بالباقي بفضل الـ Adaptive Mode
    gold_21 = page.css('.price-21').text() 
    
    print(f"✨ السعر الحالي لعيار 21 هو: {gold_21}")
    return gold_21

if __name__ == "__main__":
    get_live_gold()
