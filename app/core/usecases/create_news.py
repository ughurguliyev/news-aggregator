from stories import Success, Failure, Result, story, arguments


class CreateTrendingNews:
    """
        Creating and updating trending news 
        using Google trends
    """
    @story
    @arguments("url", "pn")
    def apply(I):
        I.validate_inputs
        I.fetch_trends
        I.fetch_news
        I.create_news
        I.finish
    
    def validate_inputs(self, ctx):
        if ctx.url:
            return Success()
        return Failure(reason="url_required")
    
    def fetch_trends(self, ctx):
        ctx.trends = self.repo.fetch_trends(ctx.pn)
        return Success()
        
    def fetch_news(self, ctx):
        ctx.fetched_news = self.repo.fetch_news(ctx.url)
        return Success() if ctx.fetched_news else Failure(reason="news_not_found")
    
    def create_news(self, ctx):
        self.repo.create_bulk_news(data=ctx.fetched_news, trends_arr=ctx.trends)
        return Success()
    
    def finish(self, ctx):
        return Result(ctx.fetched_news)

CreateTrendingNews.apply.failures(["url_required", "news_not_found"])