#!/usr/bin/env ruby

require 'pp'

class TextGenerator
  attr_accessor :tokens
  attr_accessor :max_chain_length
  
  def tokenize(text)
    token_set = []
    curr = ''
    text.each_char do |c|
      case c
      when /[A-Za-z]/
        curr << c
      when /\.|\!|\?|;|:/
        if !curr.empty?
          token_set << curr
          curr = ""
          token_set << c
        end
      else
        if !curr.empty?
          token_set << curr
          curr = ""
        end
      end
    end
    
    token_set
  end
  
  def build_hash
    @tokens.each_cons @max_chain_length do |slice| 
    end
  end
  
  def initialize(text, opts = {})
    @tokens = tokenize text
    @max_chain_length = opts[:max_chain_length] || 3
  end
  
end

text = IO.read 'timecube.txt'

gen = TextGenerator.new text, :max_chain_length => 3
p gen.tokens
p gen.max_chain_length
