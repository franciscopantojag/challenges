const denormalize = ({ primary, related, relatedName, referenceId }) => {
  const relatedMap = related.reduce((map, item) => {
    const key = item[referenceId];
    if (!map.has(key)) {
      map.set(key, []);
    }
    map.get(key).push(item);
    return map;
  }, new Map());

  return primary.map((item) => ({
    ...item,
    [relatedName]: relatedMap.get(item.id) || [],
  }));
};
