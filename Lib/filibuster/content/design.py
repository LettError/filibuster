# -*- coding: UTF-8 -*-

"""
        history
        A template for new submodules
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""

__version__ = '4.0'
__author__ = "evb"

content = {
        'design_headline':[u'<#^,design_claim#>',u'<#^,design_names#>',u'<#^,design_question#>',u'<#^,design_conclusion#>'],
        'design_section':[u'Design', u'Design', u'Design', u'Design', u'New design', u'Goodies', u'Nice to haves', u'Typography'],
        'design_ankeiler':[u'<#^,design_question#>',u'<#^,design_claim#>',u'<#^,design_work_description#>',],
        'design_sentence':[
                u'<#design_names#>: “<#design_quote#>”.',
                u'<#^,design_question#>',
                u'<#^,design_work_description#>',
                u'<#design_claim#>, <#design_question_more#>',
                u'<#design_claim#>, <#design_glue#><#design_work_description#>',
                u'<#design_claim#>, <#design_glue#><#design_work_description#>',
                u'<#design_claim#>, <#design_glue#><#design_work_description#>',
                u'<#design_claim#>, <#design_glue#><#design_counterclaim#>',
                u'<#design_claim#>, <#design_glue#><#design_counterclaim#>',
                u'<#design_claim#>, <#design_glue#><#design_counterclaim#>, <#design_glue#><#design_conclusion#>',
                u'<#design_claim#>, <#design_glue#><#design_claim#>, <#design_glue#><#design_conclusion#>',
                u'<#design_claim#>, <#design_glue#><#design_conclusion#>',
                u'<#design_claim#>, <#design_glue#><#design_conclusion#>',
                u'<#design_claim#>, <#design_glue#><#design_conclusion#>',
                ],
        'design_article_byline':[
                u'studied <#design_theory_noun#> at <#university#> and writes for <#design_magazines#>, <#design_magazines#> and <#design_magazines#>.',
                ],
        'design_article_author': [
                u'<#name_male#>'
                ],
        'design_article_title':[
                u'<#^,design_question#>',
                u'<#^,design_theory#>',
                u'<#^,design_names#> and <#design_theory#>',
                ],

        'design_focus_discipline':[
                u'graphic design', u'typography',
                ],
        'design_focus_name':[
                u'graphic design',u'typography',u'information design',u'cognitice science',u'pscychology',
                u'artificial intelligence', u'social design', u'interaction design', u'product design',
                ],
        'design_names':[
                u'Paul Renner',u'Harry Sierman',u'Walter Nikkels',u'Karel Treebus',
                u'Piet Zwart',u'Gerrit Noordzij',
                u'<#name_somewhiteguy#>',
                u'<#name_somewhiteguy#>',
                u'<#name_somewhiteguy#>',
                u'<#name_somewhiteguy#>',
                u'<#name_somewhiteguy#>',
                u'<#name_somewhiteguy#>',
                u'<#name_somewhiteguy#>',
                u'<#name_somewhiteguy#>',
                u'Gert Dumbar', u'Wim Crouwel',  u'Sjoerd de Roos',
                u'Jan van Krimpen', u'Oswald Cooper', u'Ellen Lupton', u'Dawn Barrett',
                u'Joost Swarte', u'April Greiman', u'Ann Burdick', u'Rudy Vanderlans',
                u'Max Bruinsma', u'Robin Kinross', u'Rick Poynor', u'Lorainne Wild',
                u'Louise Sandhaus', u'Brian Eno', u'David Byrne', u'David Bowie',
                u'Umberto Eco', u'Erik Spiekermann',
                u'Hannes Krüger', u'Allan Turing',
                u'Don Knuth',
                u'Andy Warhol', u'William Gibson',
                u'Wim T. Schippers',
                u'Marshal Mcluhan',
                u'Frank Lloyd Wright', u'Rem Koolhaas',
                u'Peter Saville', u'Christian Schwarz',
                u'Frank Gehry', u"Peter Bil’ak", u'Stuart Bailey', u'Paul Barnes',
                ],
        'design_worktitles_num':['', '', '', '', '', '', '', '', '', '', u' <#num_roman#>', u' <-randint(1960,2060)->'],
        'design_worktitles_parts':[u'untitled',
                u'<#^,p_figures_pop#>', u'<#^,p_oldbiz_sx#>',
                u'<#cities_USmajor#>',
                ],
        'design_worktitles':[
                u'<#^,design_worktitles_parts#><#design_worktitles_num#>',
                u'<#^,design_worktitles_parts#> and <#^,design_worktitles_parts#><#design_worktitles_num#>',
                u'<#^,design_worktitles_parts#> vs. <#^,design_worktitles_parts#><#design_worktitles_num#>',
                                ],
        'design_work_medium':[
                u'the work', u'the video installation', u'the installation',
                u'the monograph',
                u'a book', u'the piece', u'an article', u'the performance art piece',
                u'the product placement', u'the corporate information architecture', u'the information concept',
                u'personal hygiene products', u'the retrospect', u'the image store', u'the image concept',
                u'the branding',
                u'the corporate identity', u'the information strategy',u'the advertising concept', u'the product planning',
                ],
        'design_commissioner': [u'<#company#>', u'<#company_consolidated#>', u'<#corporation_japanese#>',
                u'<#bank_company#>', u'<#co_creative#>'],
        'design_work':[
                u'<#design_work_medium#> for <#design_commissioner#>',
                u'<#design_work_medium#> for <#design_commissioner#>',
                u'<#design_work_medium#> “<#design_worktitles#>”',
                u'<#design_work_medium#> “<#design_worktitles#>” (<#design_sources#>)',
                ],
        'design_work_parts':[
                u'line', u'text', u'image', u'photograph', u'hue', u'saturation', u'layout', u'page', u'material',
                u'vision', u'responsive layouts',
                u'composition', u'<#design_theory_adj#> reference', u'contrast', u'brightness',
                u'description', u'caption', u'font',

                ],
        'design_work_detail':[
                u'mix of <#design_work_parts#> and <#design_work_parts#>',
                u'relation between <#design_work_parts#> and <#design_work_parts#>',
                u'juxtaposition of <#design_work_parts#> and <#design_work_parts#>',
                u'strong line',u'vivid color',u'experimental typography', u'the new font', u'digital tool',
                u'a <#design_theory_adj#> reference if anything', u'<#design_theory_adj#> connotations',
                u'juxtaposed text', u'serifs', u'<#design_theory_noun#>',
                u'<#design_theory_adj#> imagery', u'<#design_theory_adj#> visions',
                u'composition', u'layout', u'spread'
                ],
        'design_work_description_followup':[
                '', '', '', '', '', '', '',
                u', changing from <#design_work_detail#> to <#design_work_detail#>'
                u', though the artist contends it is <#design_theory_short#>',
                 ', it is more like <#article,design_names#> or <#article,design_names#>',
                 ', more or less like <#design_names#> predicted at the time',
                u', quite similar to what <#design_names#> proposed',
                u', but that falls outside the scope of this article',
                u', something this article will look at later on',
            ],
        'design_work_description':[
                u'<#design_work_detail#> was strongly influenced by <#design_theory_short#><#design_work_description_followup#>',
                u'<#design_work#> marks the move from <#design_theory_short#> to <#design_theory_short#><#design_work_description_followup#>',
                u'the <#design_work_detail#> of <#design_theory_short#> emphasize the links to <#design_theory_short#><#design_work_description_followup#>',
                u'the <#design_work_detail#> and <#design_work_detail#> are definitely <#design_theory_short#><#design_work_description_followup#>',
                ],

        'design_location':[
                u'the workplace',
                u'<#city#>',
                u'<#design_sources#>',
                ],
        'design_magazines':[
                u'EYE', u'Form & Zweck', u'Compres', u'Druk', u'Items', u'ID', u'Wired',
                u'DotDotDot', u'Emigre', u'Hard Werken', u'LetterLetter',
                u'A.D.', u'Acro [AKPO]', u'Adbusters', u'ADGtext', u'Add!ct', u'Adobe Magazine',
                u'Affiche', u'AGD Quartal', u'AGI-NGT', u'AIGA Journal of Graphic Design',
                u'Akademische Mitteilungen', u'Aktuell Grafisk Information', u'Alphabet',
                u'Applies Arts', u'Apply', u'ARCA International', u'Argos',
                u'Architext Design', u'Ark', u'Art View', u'Baseline', u'BAT', u'Bauhaus',
                u'Blueprint', u'Bulldozer', u'Cactus', u'CMYK', u'Colors', u'Columnum', u'Da!',
                u'De Stijl', u'DaDa', u'Design Digest', u'Design Issues', u'Design Report',
                u'Domus', u'Fine Print', u'The Fleuron', u'FontZine', u'Form', u'Frieze',
                u'Fuse', u'Graficar', u'Graphis', u'Grafische Nachrichten', u'Hard Werken',
                u'Hfg Forum', u'House', u'I.D.', u'HQ High Quality', u'iM [Identity Matters]',
                u'Icographic', u'Kak',
                u'Journal of <#^,design_theory_adj#> <#^,design_theory_noun#>',
                u'Journal of <#^,design_theory_adj#> <#^,design_theory_noun#>',
                ],
        'design_sources':[
                u'<#design_magazines#> <#time_months#> <-randint(2000, 2012)->',
                ],
        'design_period':[
                u'<-randint(1900,1950)->',
                u'<-randint(18,20)->th century'
                ],
        'design_example_object':[
                u'book cover', u'advertisement', u'book', u'book on <#design_names#>',
                u'small press edition for <#name_somewhiteguy#> in <-randint(1900,1960)->'
                ],
        'design_theory_title':    [
                u'Introduction to <#design_theory#>',
                u'A critical analysis of <#design_theory#>',
                u'Dictionary of <#design_theory#>'

                ],
        'design_theory_px':[
            '', '', '', '', '', '', '', '', '', '', u'early ', u'post-', u'counter ', u'non-', u'new ', u'neo-', u'ethno-',
            ],
        'design_theory_short':[
                u'<#design_theory_px#><#design_buzzword#>',
                u'<#design_theory_px#><#design_buzzword#>',
                u'<#design_theory_px#><#design_buzzword#>',
                u'<#design_theory_px#><#design_buzzword#>',
                u'<#design_theory_px#><#design_buzzword#>',
                u'<#design_theory_px#><#design_buzzword#>',
                u'<#design_work#>',
                u'<#design_work#>',
                u'<#design_buzzword#>: <#design_work#>',
                u'<#design_buzzword#>: <#design_work#>',
                ],
        'design_theory':[
            u'<#design_theory_px#><#design_theory_adj#> yet <#design_buzzword#>',
            u'<#design_theory_px#><#design_buzzword#>',
            u'<#design_theory_px#><#design_buzzword#>',
            u'<#design_theory_px#><#design_buzzword#> in <#sci_isms#>',
            u'<#design_theory_px#><#design_buzzword#>',
            u'<#design_theory_px#><#design_buzzword#> and <#design_theory_noun#>',
            u'<#design_theory_px#><#design_buzzword#> in <#design_theory_noun#>',
                ],
        'design_nounspecific':    [
                u'typography', u'graphic design', u'design', u'architecture',
                ],
        'design_theory_noun':[
            u'resistance', u'criticism', u'experimentation', u'visualisation',
            u'performance', u'evaluation', u'assumption', u'revival', u'language',
            u'form', u'photography', u'typography', u'cliché',
            u'communication', u'modernism', u'vision', u'cognition',
            u'composition', u'detail', u'programming', u'pop-culture',
            u'finance', u'design', u'vernacular', u'revival', u'thinking', u'beauty', u'perception',
            u'verticalisation', u'improvisation', u'creation', u'philosophy',
            u'semiotics', u'semantics', u'syntax', u'reasoning', u'statement',
            u'subsidies', u'intuition',
            u'concept', u'construct', u'theory', u'theorem', u'meme', u'design theory',
                ],
        'design_theory_verb':[
                u'quantification', u'digitisation', u'midification', u'industrialisation', u'personification',
                u'deliberation', u'investigation',
                ],
        'design_theory_adj':[
            u'critical', u'virtual', u'aesthetical', u'theoretical', u'problematic', u'erratic', u'random',
            u'counter cultural', u'ethnic', u'cultural', u'investigative', u'vernacular', u'feminist',
            u'expressive', u'modernist', u'techno', u'sustainable', u'<#colors_elaborate#>', u'environmental',
            u'formal', u'technological', u'cognitive', u'relevant', u'digital', u'intellectual',
            u'recursive', u'pre-existing', u'lateral', u'material', u'immaterial',
            u'gender oriented', u'scientific', u'intuitive', u'cognitive',
                ],
        'design_theory_adj_ness':[
                u'“<#design_theory_adj#>-ness”'
                ],
        'design_work_form':    [
            u'a first example of ',
            u'an essay on',
            u'a review of', u'a study of', u'a foray into', u'an overview of'
                ],
        'design_subtitle':    [
                u'<#design_work_form#> <#design_theory#>',
                ],
        'design_title':    [
                u'<#design_theory#>: <#design_subtitle#>',
                ],
        'design_verb_to_be':    ['is', u'is', u'is', u'is', u'is', u'is', u'was',
                 ],
        'design_questionstarters':['', '', '', '', u'why ', u'how '],
        'design_question': [
                u'<#design_questionstarters#><#design_verb_to_be#> <#design_theory#> as <#design_theory_adj#> as <#design_names#> claims it <#design_verb_to_be#>?',
                u'<#design_questionstarters#><#design_verb_to_be#> <#design_theory#> really all about <#design_theory_noun#>?',
                u'<#design_questionstarters#><#design_verb_to_be#> <#design_theory#> just about <#design_theory_noun#>?',
                u'<#design_questionstarters#><#design_verb_to_be#> <#design_theory#> still relevant in the light of <#design_theory#>?',
                u'<#design_questionstarters#><#design_verb_to_be#> it hard to support <#design_theory#>?',
                u'can <#design_theory#> be seen as a part of <#design_theory#>?',
                u'<#design_questionstarters#><#design_verb_to_be#> <#design_technology#> really that <#design_theory_adj#>?',
                u'what does <#design_names#> mean with “<#design_quote#>”?',
                u'how does <#design_theory#> influence <#design_focus_discipline#>?',
                ],
        'design_question_more':[
                u'but <#design_verb_to_be#> that really the case?',
                u'but <#design_verb_to_be#> that true?',
                u'how does that reflect on <#design_theory#>?',
                u'does that affect the <#design_theory_verb#> of <#design_theory#>?',
                u'exactly why <#design_verb_to_be#> <#design_theory#>?',
                ],
        'design_buzzword': [
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_noun#> in <#design_nounspecific#>',
                u'<#design_theory_adj#> <#design_theory_noun#> in <#design_nounspecific#>',
                u'<#design_theory_adj#> <#design_theory_noun#> in <#design_nounspecific#>',
                u'<#design_theory_adj#> <#design_theory_noun#> in <#design_nounspecific#>',
                u'<#design_theory_adj#> <#design_theory_noun#> in information <#design_nounspecific#>',
                u'<#design_theory_adj#> <#design_theory_noun#>',
                u'<#design_theory_adj#> <#design_theory_verb#>',
                ],
        'design_designer': [
                u'<#design_names#>',
                ],
        'design_claim': [
                u'<#design_buzzword#> promises <#design_theory#>',
                u'<#design_buzzword#> offers insight into <#design_theory#>',
                u'<#design_buzzword#> as such does not cover <#design_theory#>',
                u'<#design_buzzword#> explained <#design_theory#>',
                u'<#design_buzzword#> founds <#design_theory#>',
                u'<#design_buzzword#> suppositions <#design_theory#>',
                u'<#design_theory#> cannot replace <#design_theory#> as a <#design_theory_noun#>',
                u'<#design_theory#> <#design_verb_to_be#> <#design_theory_adj#>',
                u'<#design_theory#> <#design_verb_to_be#> <#design_theory_adj#>, not <#design_theory_adj#>',
                u'<#design_buzzword#> as described by <#design_names#> <#design_verb_to_be#> not <#design_theory_adj#>',
                u'the role of <#design_technology#> <#design_verb_to_be#> <#design_word_thingy#><#design_theory_adj#>',
                u'<#design_theory#> puts <#design_theory_noun#> in a <#design_theory_adj#> perspective',
                u'in <#design_sources#> <#design_names#> claimed that “<#design_quote#>”',
                u'the work of <#design_names#> in <#design_location#> is an example of <#design_theory#>',
                u'looking at <#design_theory#>, the <#design_theory_noun#> becomes <#design_theory_adj#>',
                u'studying <#design_theory#>, the <#design_theory_noun#> becomes <#design_theory_adj#> instead',
                u'<#design_work#> <#design_ref#> brings <#design_theory_noun#> into <#design_theory#>',
                u'<#design_work#> shows <#design_theory_noun#> has a place in <#design_theory#>',
                u'<#design_work#> is one of <#design_names#> most important projects',
                ],
        'design_ref':    [
                u', (<#design_names#>: <#^,refthing#>, <-randint(1900, 1950)->, <-randint(1950,2000)->)',
                u', (<#design_names#> on <#^,refthing#> <-randint(1950,2000)->)',
                u', (<#^,refthing#>, <-randint(1920,2000)->)',
                ],
        'refthing':['realism', 'language', 'philosophy', 'critical thinking', 'internet', "AI", "<#design_magazines#>" ],
        'design_counterclaim':    [
                u'the problem with <#^,design_buzzword#>  is that <#design_claim#>',
                u'rather, <#design_buzzword#> is explained by <#design_claim#>',
                u'rather, <#design_claim#>',
                u'but <#design_claim#>',
                u'but how about <#design_work#> and <#design_work#>',
                u'but how to explain <#design_work#> in the context of <#design_buzzword#>',
                u'and <#design_claim#>',
                u'on the other hand, <#design_claim#>',
                u'<#design_question#>',
                u'<#design_question#>',
                u'<#design_question_more#>',
                ],
        'design_argument':    [
                u'<#design_names#> stated: “<#design_claim#>”',
                u'<#design_names#> wrote: “<#design_claim#>”',
                u'<#design_names#> writes: “<#design_claim#>”',
                u'<#design_names#> observes: “<#design_claim#>”',
                u'<#design_names#> observed: “<#design_claim#>”',
                u'<#design_names#> remarks: “<#design_claim#>”',
                u'<#design_names#> proposed: “<#design_claim#>”',
                u'<#design_names#> suggested: “<#design_claim#>”',
                u'<#design_names#> says about this: “<#design_work_description#>”',
                u'<#design_names#> <#design_verb#> <#design_theory_adj_ness#>',
                ],
        'design_word_thingy':    [
                u'merely ', u'sometimes ', u'never ', '', '', '', '', '', '', '', '',
                ],
        'design_word_thingy2':    [
                u'enough ', u'anymore ', '', '', '', '', '', '', '', '',
                ],
        'design_verb':    [
                u'strongly believed in',
                u'liked the idea of',
                u'publicly supported',
                u'seriously considered',
                ],
        'design_conclusion':[
                u'later <#design_names#> proved <#design_theory_noun#> <#design_verb_to_be#> <#design_theory#>',
                u'current developments in <#design_technology#> point to the contrary',
                u'an interaction with <#design_theory#> is necessary',
                u'<#design_theory#> <#design_verb_to_be#> about <#design_theory_noun#>',
                u'<#design_theory#> certainly <#design_verb_to_be#> not just <#design_theory_adj#>',
                u'<#design_counterclaim#>',
                u'<#design_counterclaim#>',
                u'<#design_counterclaim#>',
                u'<#design_claim#>',
                u'<#design_claim#>',
                u'<#design_claim#>',
                ],
        'design_quote_stopper':    [
                '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '',
                u' [...]',
                u' [sic]',
                u' [ed.]',
                ],
        'design_quote_starter':    [
                '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '',
                u'[it seems] ', u'[I think] ' , u'[it follows] ', u'[assume] '
                ],
        'design_quote_infrequent':[
                u'<#design_theory_noun#> is dead',
                u'<#dibbi=design_theory_noun#><#dibbi#> is <#dibbi#> is <#dibbi#>',
                ],
        'design_quote_glue':['is like', u'was', u'is not at the same as', u'can be compared to', u'should be treated the same as'],
        'design_quote':[
                u"I don’t like <#design_technology#>",
                "I hate <#design_technology#>",
                u'you can’t compare <#design_theory_noun#> with <#design_theory_noun#>',
                u'<#design_quote_infrequent#>',
                u'<#design_quote_infrequent#>',
                u'my take on that was always that <#design_theory#>',
                u'I always said that <#design_theory#>',
                #'I don�t think that <#design_theory#> is like <#odd_action#><#design_quote_stopper#>',
                #'I like <#odd_action#>',
                #'<#design_technology#> is <#odd_action#>',
                #'I like <#odd_action#>',
                #'<#design_technology#> is <#odd_action#>',
                #'I like <#odd_action#>',
                #'<#design_technology#> is <#odd_action#>',
                #'I like <#odd_action#>',
                #'<#design_technology#> is <#odd_action#>',
                u'<#design_theory#> is nonsense',
                #'<#design_quote_starter#>that <#design_theory#> <#design_quote_glue#> <#odd_action#><#design_quote_stopper#>',
                u'<#design_quote_starter#>that <#design_claim#> and <#design_claim#><#design_quote_stopper#>',
                u'<#design_quote_starter#>that <#design_theory#> <#design_quote_glue#> <#design_theory_adj#><#design_quote_stopper#>',
                u'<#design_quote_starter#><#design_theory_noun#> <#design_verb_to_be#> <#design_theory_noun#><#design_quote_stopper#>',
                u'<#design_quote_starter#><#design_theory_noun#> <#design_verb_to_be#> all about <#design_theory_noun#><#design_quote_stopper#>',
                ],
        'design_technology':[
                u'desktop-publishing', u'critical thought', u'early <#design_theory_noun#>' , u'late <#design_theory_noun#>'
                u'movable type', u'breathmints', u'information design',
                u'language', u'the internet', u'the web', u'the marketplace', u'Apple Macintosh', u'the digital tool',
                u"responsive", "IOT", "the dark web", "rectangles"
                ],
        'design_interjection':    [
            #    '', '', '', '', '', '', '', '', '',
                u', <#design_names#> said as much in <-randint(1900,1950)->,',
                u', <#design_theory_adj#> itself does not explain it,',
                u', without his knowledge,'
                ],
        'design_glue':    [
                '', '', '', '', '', '', '', '', '', '',
                u'so ', u'therefore ', u'but ', u'eventhough ', u'though ', u'and ', u'rather ',
                ],
        'design_sentencetest':[
            u'<#design_claim#>, <#design_glue#> <#design_claim#><#design_interjection#>, <#design_glue#> <#design_conclusion#>',
            ],
        }


if __name__ == "__main__":
    print(content.keys())