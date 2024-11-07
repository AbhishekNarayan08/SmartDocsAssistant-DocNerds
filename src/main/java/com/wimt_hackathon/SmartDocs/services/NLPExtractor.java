package com.wimt_hackathon.SmartDocs.services;

import opennlp.tools.namefind.NameFinderME;
import opennlp.tools.namefind.TokenNameFinderModel;
import opennlp.tools.tokenize.WhitespaceTokenizer;
import opennlp.tools.util.Span;

import java.io.FileInputStream;

public class NlpExtractor {
    private NameFinderME nameFinder;

    public NlpExtractor() throws Exception {
        TokenNameFinderModel model = new TokenNameFinderModel(new FileInputStream("en-ner-person.bin"));
        nameFinder = new NameFinderME(model);
    }

    public String[] extractNames(String text) {
        String[] tokens = WhitespaceTokenizer.INSTANCE.tokenize(text);
        Span[] nameSpans = nameFinder.find(tokens);
        String[] names = Span.spansToStrings(nameSpans, tokens);
        return names;
    }
}
