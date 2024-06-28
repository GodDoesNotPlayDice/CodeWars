def reverse_words(str)
    str.gsub(/\S+/, &:reverse)
  end
puts reverse_words("The quick brown fox jumps over the lazy dog.")
