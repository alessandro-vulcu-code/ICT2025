function decodeUplink(input) {
    return {
      data: {
        message: input.bytes.map(c => String.fromCharCode(c)).join('')
      },
      warnings: [],
      errors: []
    };
  }