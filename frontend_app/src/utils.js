/**
 * @param {String} url
 */
export function getHost(url) {
  return url.replace(/(^https?:\/\/)?(www\.)?/, '').replace(/\/(.+)?$/, '')
}

/**
 * @param {number} timestamp
 * @returns {number}
 */
export function getHoursDifferenceFromNow(timestamp) {
  const hours = (new Date().getTime() - timestamp * 1000) / (60 * 60 * 1000)
  return +hours.toFixed(0)
}
